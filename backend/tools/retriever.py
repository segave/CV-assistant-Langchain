from dotenv import load_dotenv

load_dotenv(override=True)

from typing import Any, Dict, List

from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.tools import Tool
from langchain.prompts import ChatPromptTemplate
import streamlit as st

import os

# Load the environment variable for Pinecone index
INDEX_NAME = os.environ["INDEX_NAME"]
NAMESPACE = os.environ["NAMESPACE"]


# Define the retriever function
def create_flexible_retriever_tool(
    temperature: float = 0,
    search_kwargs: dict = {"k": 4},
    model_name: str = st.session_state.get("selected_model", "gpt-4o-mini"),
):
    """
    Creates a flexible retriever tool capable of handling multiple search types.

    Args:
        temperature: Float value to control randomness in responses
        search_kwargs: Dictionary of search parameters (e.g., {"k": 4} for top 4 results)
        model_name: Name of the OpenAI model to use

    Returns:
        Tool: A retriever tool ready to handle multiple search types dynamically.
    """
    if not INDEX_NAME:
        raise ValueError("INDEX_NAME environment variable is not set")

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    docsearch = PineconeVectorStore(
        index_name=INDEX_NAME, embedding=embeddings, namespace=NAMESPACE
    )
    chat = ChatOpenAI(verbose=True, temperature=temperature, model_name=model_name)

    # Define prompts for different types of searches
    prompts = {
        "skills": ChatPromptTemplate.from_template(
            """Given the chat history: {chat_history}
            And the user's question: {input}
            Rephrase the question to find candidates with specific technical skills. 
            Focus on programming languages, tools, and technical expertise.
            In your response, always include:
            1. The name of the candidate (from metadata["name"])
            2. The specific skills they have
            3. Any relevant context about their experience"""
        ),
        "name": ChatPromptTemplate.from_template(
            """Given the chat history: {chat_history}
            And the user's question: {input}
            Rephrase the question to search for candidates by their name.
            In your response, include:
            1. The candidate's full name (from metadata["name"])
            2. Key information found about them"""
        ),
        "general": ChatPromptTemplate.from_template(
            """Given the chat history: {chat_history}
            And the user's question: {input}
            Search for relevant information in the CVs.
            Always include the candidate's name (from metadata["name"]) in your response."""
        ),
    }

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    stuff_documents_chain = create_stuff_documents_chain(chat, retrieval_qa_chat_prompt)

    def flexible_func(input_data: Dict[str, Any] | str) -> Dict[str, Any]:
        """Process input which can be either a string or a dictionary."""
        # Handle string input by converting to dict
        if isinstance(input_data, str):
            try:
                # Try to parse as JSON if it's a string representation of a dict
                import json

                input_data = json.loads(input_data)
            except json.JSONDecodeError:
                # If not JSON, treat as a general query
                input_data = {
                    "input": input_data,
                    "search_type": "general",
                    "chat_history": [],
                }

        # Now process as dictionary
        search_type = input_data.get("search_type", "general")
        query = input_data.get(
            "input", input_data if isinstance(input_data, str) else ""
        )
        chat_history = input_data.get("chat_history", [])

        prompt = prompts.get(search_type, prompts["general"])

        history_aware_retriever = create_history_aware_retriever(
            llm=chat,
            retriever=docsearch.as_retriever(search_kwargs=search_kwargs),
            prompt=prompt,
        )

        retrieval_chain = create_retrieval_chain(
            retriever=history_aware_retriever, combine_docs_chain=stuff_documents_chain
        )

        try:
            result = retrieval_chain.invoke(
                {"input": query, "chat_history": chat_history}
            )
            return result
        except Exception as e:
            return {"answer": f"Error during retrieval: {str(e)}"}

    return Tool(
        name="Flexible_CV_Retriever",
        func=flexible_func,
        description="""Search through a CV database to retrieve candidates based on criteria like skills, names, or general information.

    **Input Format**:
    - String: Treated as a general search query.
    - Dictionary: 
      - "input" (required): The search query string.
      - "search_type" (optional): One of ["skills", "name", "general"]. Defaults to "general".
      - "chat_history" (optional): List of previous interactions for additional context.

    **Examples**:
    1. Search by skills: {"input": "Python and AWS experience", "search_type": "skills"}
    2. Search by name: {"input": "John Smith", "search_type": "name"}
    3. General search: {"input": "Candidates with startup experience"}

    **Output**: Returns relevant CV information matching the criteria.""",
    )


# Example of usage
if __name__ == "__main__":
    retriever_tool = create_flexible_retriever_tool()
    test_queries = [
        {"input": "Find developers with Python experience", "search_type": "skills"},
        # {"input": "Find someone named Carlos Galán", "search_type": "name"},
        {
            "input": "Find people qho has attended to  Business School of Economics",
            "search_type": "general",
        },
    ]

    for query in test_queries:
        print(f"\nSearching for: {query['input']} (Type: {query['search_type']})")
        print("-" * 50)
        response = retriever_tool.func(query)
        print(f"\nResponse:")
        print(response.get("answer", "No answer found."))
