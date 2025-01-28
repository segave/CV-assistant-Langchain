from langchain.tools import Tool
from backend.tools.retriever.tool import create_flexible_retriever_tool
from backend.tools.help_tool import HelpTool
from backend.agents.email_writer import create_email_writer_agent
from backend.tools.job_matcher.tool import JobMatcherTool
from backend.tools.email_sender.tool import EmailSenderTool

def create_tools_suite():
    """Creates and configures all available tools."""
    return [
        create_flexible_retriever_tool(),
        HelpTool(),
        Tool(
            name="email_writer",
            func=lambda x: create_email_writer_agent().invoke({
                "input": x,
                "chat_history": []
            }),
            description="""Writes personalized job opportunity emails to candidates. Use this tool when you want to:
    - Generate a professional email inviting a candidate to apply
    - Write a job opportunity email based on candidate's background
    Input should be the candidate's background information."""
        ),
        JobMatcherTool(),
        EmailSenderTool(),
    ] 