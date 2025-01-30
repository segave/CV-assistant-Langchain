from typing import Any
from langchain.tools import BaseTool
from typing import Optional


class HelpTool(BaseTool):
    name: str = "help"
    description: str = """Provides help information about the application's features and how to use them."""

    def _run(self, query: str = "") -> str:
        """Return help information about the application."""
        return """
        Welcome to the AI Recruiter Assistant! Here's how to use the main features:
        
        1. CV Analysis
        - Upload CV documents in PDF format using the document uploader
        - The system will automatically extract and analyze the candidate's information
        - You can view and manage uploaded documents in the document list
        
        2. Chat Interface
        - Use the chat to ask questions about candidates
        - Request analysis of specific skills or experience
        - Generate personalized emails for candidates
        
        3. Profile Management
        - Set up your recruiter profile in the User Profile tab
        - Configure job requirements and preferences
        - Update company information used in communications
        
        4. Email Management
        - Configure email credentials in the Email Credentials tab
        - Generate personalized emails through the chat interface
        - View and manage generated emails in the Generated Emails tab
        - Edit email content, subject, and recipients before sending
        - Send emails directly from the interface
        
        5. Job Description
        - Add and update job descriptions in the Job Description tab
        - Use these descriptions for matching candidates
        
        Tips:
        - Keep your profile and job descriptions up to date for better results
        - Use specific questions in the chat for more accurate responses
        - Review generated emails before sending them
        - You can edit any generated email before sending by clicking the "Edit" button
        - Successfully sent emails are automatically removed from the history
        
        Need more help? Just ask specific questions in the chat!
        """

    async def _arun(self, query: str = "") -> Any:
        """Async implementation"""
        raise NotImplementedError("This tool doesn't support async execution")
