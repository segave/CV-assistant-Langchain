import streamlit as st
from typing import Dict

def get_smtp_credentials() -> Dict[str, str]:
    """Retrieves and validates SMTP credentials."""
    sender_email = st.session_state.get("email")
    password = st.session_state.get("password")
    
    if not sender_email or not password:
        st.error("Email credentials not provided")
        raise ValueError("Missing email credentials")
    
    return {
        "email": sender_email,
        "password": password,
        "smtp_server": 'smtp.gmail.com' if '@gmail.com' in sender_email else 'smtp-mail.outlook.com',
        "port": 587
    } 