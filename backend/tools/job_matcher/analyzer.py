import streamlit as st
from .llm_config import create_matcher_llm
from backend.prompts.job_matcher_prompts import ANALYSIS_PROMPT

def analyze_candidates(candidates_info: str) -> str:
    """Analyzes candidates matches using LLM."""
    llm = create_matcher_llm()
    
    response = llm.invoke(
        ANALYSIS_PROMPT.format_messages(
            position_title=st.session_state.get('position_title', ''),
            description=st.session_state.get('description', ''),
            department=st.session_state.get('department', ''),
            location=st.session_state.get('location', ''),
            contract_type=st.session_state.get('contract_type', ''),
            salary_range=st.session_state.get('salary_range', ''),
            key_requirements=st.session_state.get('key_requirements', ''),
            benefits=st.session_state.get('benefits', ''),
            candidates_info=candidates_info,
        )
    )
    
    return response.content 