from langchain.tools import BaseTool
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st
from typing import Dict, Any, Union
import json

class EmailSenderTool(BaseTool):
    name: str = "email_sender"
    description: str = """Sends an email to a candidate. Use this tool when:
    - You want to send the email that was just written
    - You have the candidate's email address
    Input should be a dictionary with 'email_data' containing 'to_email', 'subject', and 'body'.
    You always need the confirmation from the user to call this tool.
    """
    
    def _run(self, input_data: Union[Dict[str, Any], str]) -> str:
        """
        Sends an email using stored credentials.
        """
        try:
            # Convert string to dict if necessary
            if isinstance(input_data, str):
                try:
                    input_data = eval(input_data) 
                except:
                    st.error("Could not parse input data")
                    return "Error: Invalid input format"
            
            # Extract email data
            email_data = input_data.get("email_data", {})
            if not email_data:
                st.error("No email data provided")
                return "Error: No email data provided"
            
            # Retrieve stored credentials
            sender_email = st.session_state.get("email")
            password = st.session_state.get("password")
            
            if not sender_email or not password:
                st.error("Email credentials not provided")
                return "Error: Missing email credentials"
            
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = email_data['to_email']
            msg['Subject'] = email_data['subject']
            msg.attach(MIMEText(email_data['body'], 'plain'))
            
            # Determine SMTP server based on email domain
            smtp_server = 'smtp.gmail.com' if '@gmail.com' in sender_email else 'smtp-mail.outlook.com'
            
            # Connect to SMTP server
            server = smtplib.SMTP(smtp_server, 587)
            server.starttls()
            
            # Login
            server.login(sender_email, password)
            
            # Send email
            server.send_message(msg)
            server.quit()
            
            st.success(f"Email sent successfully to {email_data['to_email']}")
            return f"Email sent successfully to {email_data['to_email']}"
        
        except Exception as e:
            st.error(f"Error sending email: {str(e)}")
            return f"Error: {str(e)}"

    async def _arun(self, query: str) -> Any:
        """Async implementation"""
        raise NotImplementedError("This tool doesn't support async execution")

def main():
    # Example email data
    email_data = {
        "to_email": "sergiogalianavelasco@gmail.com",
        "subject": "Test Email",
        "body": "This is a test email sent from the EmailSenderTool."
    }
    
    # Create an instance of the tool
    email_sender = EmailSenderTool()
    
    # Run the tool with the example data
    result = email_sender._run({"email_data": email_data})
    print(result)

if __name__ == "__main__":
    main()

