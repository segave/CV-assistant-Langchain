import smtplib
from email.mime.multipart import MIMEMultipart
import streamlit as st
from typing import Dict

def send_email(credentials: Dict[str, str], message: MIMEMultipart) -> None:
    """Handles SMTP connection and email sending."""
    try:
        server = smtplib.SMTP(credentials["smtp_server"], credentials["port"])
        server.starttls()
        server.login(credentials["email"], credentials["password"])
        server.send_message(message)
        server.quit()
        st.success(f"Email sent successfully to {message['To']}")
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        raise 