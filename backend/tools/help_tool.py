from typing import Any
from langchain.tools import BaseTool
from typing import Optional


class HelpTool(BaseTool):
    name: str = "help_tool"
    description: str = (
        "Provides information about how to use the application and its features"
    )

    def _run(self, query: str = "") -> str:
        """Executes the help tool"""
        return """
🤖 Welcome to the CV AI Assistant

This application allows you to:

1. Query CVs
   - Ask questions about specific candidates
   - Search by name, skills, or experience
   - Get detailed profile information

2. Job Matching
   - Find candidates that match job requirements
   - Get detailed analysis of candidate matches
   - View match percentages for each candidate
   - Identify strongest candidates for the position

3. Email Communication
   - Generate personalized job opportunity emails
   - Contact candidates about the position
   - Highlight relevant experience matches
   - Include professional signatures automatically

4. Types of questions you can ask:
   - "What experience does [name] have in [technology]?"
   - "What is [name]'s academic background?"
   - "Who has experience in [technology]?"
   - "Find candidates with skills in [area]"
   - "Find matching candidates for the position"
   - "Write an email to [candidate] about the job opportunity"
   - "Who would be the best fit for this position?"

5. Usage tips:
   - Be specific in your questions
   - You can ask about multiple aspects in one query
   - The assistant maintains conversation context
   - Use 'match' or 'find candidates' for job matching
   - Use 'write email' or 'contact' for email generation

To get started, simply type your question in the chat.
"""

    async def _arun(self, query: str = "") -> Any:
        """Async implementation"""
        raise NotImplementedError("This tool doesn't support async execution")
