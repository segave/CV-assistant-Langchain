from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_pinecone import PineconeVectorStore
from langchain.schema import Document
from pinecone import Pinecone
from typing import Optional
from dotenv import load_dotenv
import os
import glob
import re

# Load environment variables
load_dotenv(override=True)

# Verificar variables de entorno críticas
NAMESPACE = os.getenv("NAMESPACE")
INDEX_NAME = os.getenv("INDEX_NAME")
if not NAMESPACE or not INDEX_NAME:
    raise ValueError(
        "Missing required environment variables: NAMESPACE and/or INDEX_NAME"
    )

print(f"Using namespace: {NAMESPACE}")
print(f"Using index: {INDEX_NAME}")

# Define el modelo de lenguaje
chat = ChatOpenAI(model_name="gpt-4o", temperature=0)

# Define text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=100, separators=["\n\n", "\n", ".", ",", " ", ""]
)


def extract_email(text: str) -> str:
    """Extract email from text using regex"""
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(email_pattern, text)
    return match.group(0) if match else ""


def load_pdf_content_as_text(pdf_path: str) -> str:
    """Load PDF content as text using PyPDFLoader."""
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    return "\n".join(page.page_content for page in pages)


def extract_name_using_ai(file_name: str, document_text: str) -> Optional[str]:
    """
    Usa un modelo de lenguaje para extraer el nombre de una persona a partir del nombre del archivo
    y del contenido del documento.
    """
    system_prompt = """You are an expert at extracting names from CVs. 
    Your task is to extract the full name of the person from the CV.
    Respond ONLY with the full name, nothing else."""

    user_prompt = f"""Extract the full name from this CV.
    File name: {file_name}
    First part of CV:
    {document_text[:1000]}
    """

    try:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        response = chat.invoke(messages)

        # Extraer el contenido del mensaje
        extracted_name = response.content

        # Validar el nombre extraído
        if extracted_name and len(extracted_name.split()) >= 2:
            return extracted_name.strip()
        return None

    except Exception as e:
        print(f"Error using AI to extract name: {str(e)}")
        return None


def process_pdfs_and_create_vectorstore_with_ai(pdf_folder, index_name, namespace):
    """
    Procesa PDFs y usa IA para extraer nombres, dividiendo en chunks y subiendo a Pinecone.
    """
    # Initialize Pinecone
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

    # Initialize embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # Listar todos los archivos PDF
    pdf_files = glob.glob(os.path.join(pdf_folder, "*.pdf"))

    all_documents = []

    for pdf_file in pdf_files:
        try:
            # Nombre del archivo
            file_name = os.path.basename(pdf_file)
            print(f"Processing: {file_name}")

            # Cargar el contenido del documento
            document_text = load_pdf_content_as_text(pdf_file)

            # Extraer el nombre usando IA
            person_name = extract_name_using_ai(file_name, document_text)

            # Extraer email del contenido
            email = extract_email(document_text)

            if not person_name:
                print(f"Could not extract name from {file_name}, using 'Unknown'")
                person_name = "Unknown"
            else:
                print(f"Extracted name: {person_name}")

            if email:
                print(f"Found email: {email}")

            # Procesar y dividir en chunks
            chunks = text_splitter.split_text(document_text)

            # Create proper Document objects
            for chunk in chunks:
                doc = Document(
                    page_content=chunk,
                    metadata={"name": person_name, "source": file_name, "email": email},
                )
                all_documents.append(doc)

        except Exception as e:
            print(f"Error processing {pdf_file}: {str(e)}")
            continue

    if all_documents:
        # Subir a Pinecone
        PineconeVectorStore.from_documents(
            all_documents, embeddings, index_name=index_name, namespace=namespace
        )
        print(
            f"Successfully uploaded {len(all_documents)} chunks to Pinecone (namespace: '{namespace}')."
        )
    else:
        print("No documents were processed successfully.")


if __name__ == "__main__":
    # Ejemplo de uso
    process_pdfs_and_create_vectorstore_with_ai(
        pdf_folder="ingestion/DOCS", index_name=INDEX_NAME, namespace=NAMESPACE
    )
