import streamlit as st

def build_search_query() -> str:
    """Builds the search query from job requirements."""
    return f"""
    Position: {st.session_state.get('position_title', '')}

    Description:
    {st.session_state.get('description', '')}

    Department: {st.session_state.get('department', '')}
    Location: {st.session_state.get('location', '')}
    Contract: {st.session_state.get('contract_type', '')}
    Salary Range: {st.session_state.get('salary_range', '')}

    Key Requirements:
    {st.session_state.get('key_requirements', '')}

    Benefits:
    {st.session_state.get('benefits', '')}
    """ 