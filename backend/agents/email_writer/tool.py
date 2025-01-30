from typing import Union, Dict, Any

from .llm_config import create_email_llm
from .template_generator import generate_email_template
import streamlit as st

def write_email(candidate_info: Union[str, Dict[str, Any]]) -> dict:
    """Write a personalized email based on candidate information.
    
    Args:
        candidate_info (Union[str, Dict[str, Any]]): Information about the candidate.
            Can be either a string description or a dictionary with structured data.
    
    Returns:
        dict: A dictionary containing:
            - email_content (str): The generated email body
            - email_data (dict): Structured data including to_email, subject, and body
    """
    # Create LLM
    llm = create_email_llm()
    
    # Generate the email content using internal helper functions
    email_data = generate_email_template(candidate_info, llm)
    
    # Extract email if candidate_info is a dictionary
    if isinstance(candidate_info, dict):
        email_data["to_email"] = candidate_info.get("metadata", {}).get("email", "")
    
    # Add email to history in session state
    if "email_history" not in st.session_state:
        st.session_state["email_history"] = []
    
    email_entry = {
        "to_email": email_data["to_email"],
        "subject": email_data["subject"],
        "body": email_data["email_content"]
    }
    st.session_state["email_history"].append(email_entry)
    
    return {
        "email_content": email_data["email_content"],
        "email_data": {
            "to_email": email_data["to_email"],
            "subject": email_data["subject"],
            "body": email_data["email_content"]
        }
    } 