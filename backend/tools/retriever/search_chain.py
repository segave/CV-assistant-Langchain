from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_openai import ChatOpenAI
import streamlit as st
from backend.prompts.retriever_prompts import SEARCH_PROMPTS
from .vector_store import create_vector_store

def create_search_chain(search_type: str, search_kwargs: dict):
    """Creates a search chain for the specified type."""
    chat = ChatOpenAI(
        verbose=True,
        temperature=search_kwargs["llm_config"].get("temperature", 0),
        model_name=st.session_state.get("selected_model", "gpt-4o-mini")
    )
    
    vector_store = create_vector_store()
    prompt = SEARCH_PROMPTS.get(search_type, SEARCH_PROMPTS["general"])
    
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    stuff_documents_chain = create_stuff_documents_chain(chat, retrieval_qa_chat_prompt)
    
    history_aware_retriever = create_history_aware_retriever(
        llm=chat,
        retriever=vector_store.as_retriever(search_kwargs=search_kwargs["search_kwargs"]),
        prompt=prompt,
    )
    
    return create_retrieval_chain(
        retriever=history_aware_retriever,
        combine_docs_chain=stuff_documents_chain
    ) 