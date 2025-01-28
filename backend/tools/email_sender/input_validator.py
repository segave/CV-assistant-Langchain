from typing import Dict, Any, Union
import streamlit as st

def validate_email_data(input_data: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validates and formats input data."""
    if isinstance(input_data, str):
        try:
            input_data = eval(input_data)
        except:
            st.error("Could not parse input data")
            raise ValueError("Invalid input format")
    
    email_data = input_data.get("email_data", {})
    if not email_data:
        st.error("No email data provided")
        raise ValueError("No email data provided")
    
    return email_data 