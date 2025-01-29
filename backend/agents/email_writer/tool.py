from typing import Union, Dict, Any

from .llm_config import create_email_llm
from .template_generator import generate_email_template

def write_email(candidate_info: Union[str, Dict[str, Any]]) -> dict:
    """Tool that writes a personalized email based on candidate information."""
    # Create LLM
    llm = create_email_llm()
    
    # Generate the email content using internal helper functions
    email_data = generate_email_template(candidate_info, llm)
    
    # Extract email if candidate_info is a dictionary
    if isinstance(candidate_info, dict):
        email_data["to_email"] = candidate_info.get("metadata", {}).get("email", "")
    
    return {
        "email_content": email_data["email_content"],
        "email_data": {
            "to_email": email_data["to_email"],
            "subject": email_data["subject"],
            "body": email_data["email_content"]
        }
    } 