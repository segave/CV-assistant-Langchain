from langchain_openai import ChatOpenAI
import streamlit as st

def create_orchestrator_llm():
    """Creates and configures the LLM for the orchestrator."""
    return ChatOpenAI(
        temperature=0, 
        model=st.session_state.get("selected_model", "gpt-4o-mini")
    ) 