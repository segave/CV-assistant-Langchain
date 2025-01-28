from langchain_openai import ChatOpenAI
import streamlit as st

def create_email_llm():
    """Creates and configures the LLM for email writing."""
    return ChatOpenAI(
        temperature=0.7,
        model=st.session_state.get("selected_model", "gpt-4o-mini")
    ) 