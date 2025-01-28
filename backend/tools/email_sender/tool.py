from langchain.tools import BaseTool
from typing import Dict, Any, Union
from .input_validator import validate_email_data
from .credentials_manager import get_smtp_credentials
from .message_builder import create_email_message
from .smtp_handler import send_email

class EmailSenderTool(BaseTool):
    name: str = "email_sender"
    description: str = """Sends an email to a candidate. Use this tool when:
    - You want to send the email that was just written
    - You have the candidate's email address
    Input should be a dictionary with 'email_data' containing 'to_email', 'subject', and 'body'.
    You always need the confirmation from the user to call this tool.
    """
    
    def _run(self, input_data: Union[Dict[str, Any], str]) -> str:
        """Sends an email using stored credentials."""
        try:
            # Validate input
            email_data = validate_email_data(input_data)
            
            # Get credentials
            credentials = get_smtp_credentials()
            
            # Create message
            message = create_email_message(credentials["email"], email_data)
            
            # Send email
            send_email(credentials, message)
            
            return f"Email sent successfully to {email_data['to_email']}"
            
        except Exception as e:
            return f"Error: {str(e)}"

    async def _arun(self, query: str) -> Any:
        """Async implementation"""
        raise NotImplementedError("This tool doesn't support async execution") 