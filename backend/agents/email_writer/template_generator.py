from typing import Union, Dict, Any
import streamlit as st
from langchain.output_parsers import StructuredOutputParser
from backend.prompts.schemas import EMAIL_SCHEMAS
from backend.prompts.email_prompts import EMAIL_PROMPT
from langchain_openai import ChatOpenAI

def generate_email_template(candidate_info: Union[str, Dict[str, Any]], llm: ChatOpenAI) -> dict:
    """Generates email content using templates and LLM."""
    # Extract content if candidate_info is a dictionary
    if isinstance(candidate_info, dict):
        candidate_info = candidate_info.get("page_content", "")

    # Create parser
    output_parser = StructuredOutputParser.from_response_schemas(EMAIL_SCHEMAS)
    format_instructions = output_parser.get_format_instructions()

    # Get recruiter information from session state
    recruiter_info = f"""
    Name: {st.session_state.get("name", "")}
    Position: {st.session_state.get("position", "")}
    Company: {st.session_state.get("company", "")}
    Email: {st.session_state.get("email", "")}
    Phone: {st.session_state.get("phone", "")}
    """
    
    # Generate email content using the provided LLM
    response = llm.invoke(
        EMAIL_PROMPT.format_messages(
            format_instructions=format_instructions,
            recruiter_info=recruiter_info,
            position_title=st.session_state.get("position_title", ""),
            description=st.session_state.get("description", ""),
            department=st.session_state.get("department", ""),
            location=st.session_state.get("location", ""),
            contract_type=st.session_state.get("contract_type", ""),
            salary_range=st.session_state.get("salary_range", ""),
            key_requirements=st.session_state.get("key_requirements", ""),
            benefits=st.session_state.get("benefits", ""),
            candidate_info=candidate_info,
        )
    )
    
    # Parse the response
    try:
        return output_parser.parse(response.content)
    except Exception as e:
        st.error(f"Error parsing email response: {str(e)}")
        return {
            "email_content": response.content,
            "subject": f"Job Opportunity at {st.session_state.get('company', '')}",
            "to_email": ""
        } 