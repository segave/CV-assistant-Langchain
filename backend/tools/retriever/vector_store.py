from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from .config import INDEX_NAME, NAMESPACE

def create_vector_store():
    """Creates and returns the vector store instance."""
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    return PineconeVectorStore(
        index_name=INDEX_NAME,
        embedding=embeddings,
        namespace=NAMESPACE
    ) 