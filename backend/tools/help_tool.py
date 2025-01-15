from typing import Any
from langchain.tools import BaseTool
from typing import Optional


class HelpTool(BaseTool):
    name: str = "help"
    description: str = """Use this tool to get help about:
    - Available commands and tools
    - How to use specific features
    - Required configurations"""

    def _run(self, query: str = "") -> str:
        """Executes the help tool"""
        return """I can help you with the following tasks:

1. Search and Retrieve CVs
   - Search by name: "Find CV for John Doe"
   - Search by skills: "Find candidates with Python experience"
   - Search by location: "Find candidates in Madrid"

2. Write Professional Emails
   - Generate personalized job opportunity emails
   - Write invitation emails to candidates

3. Job Matching
   - Compare candidate profiles with job requirements
   - Get matching scores and analysis
   
4. General Help
   - Ask about any feature or capability
   - Get guidance on how to use specific tools

To get started, you can:
1. Upload CVs using the document uploader
2. Configure your recruiter profile and job details
3. Set up email credentials to enable sending
4. Start searching for candidates or writing emails

How can I assist you today?"""

    async def _arun(self, query: str = "") -> Any:
        """Async implementation"""
        raise NotImplementedError("This tool doesn't support async execution")
