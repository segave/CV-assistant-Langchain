from langchain.tools import Tool
from backend.tools.registry import ToolRegistry
from backend.tools.retriever.tool import create_flexible_retriever_tool
from backend.tools.help_tool import HelpTool
from backend.agents.email_writer import create_email_writer_agent
from backend.tools.job_matcher.tool import JobMatcherTool
from backend.tools.email_sender.tool import EmailSenderTool

def register_default_tools():
    """Register all default tools in the registry."""
    ToolRegistry.register("retriever", create_flexible_retriever_tool)
    ToolRegistry.register("help", lambda: HelpTool())
    ToolRegistry.register("job_matcher", lambda: JobMatcherTool())
    ToolRegistry.register("email_sender", lambda: EmailSenderTool())
    ToolRegistry.register(
        "email_writer",
        lambda: Tool(
            name="email_writer",
            func=lambda x: create_email_writer_agent().invoke({
                "input": x,
                "chat_history": []
            }),
            description="""Writes personalized job opportunity emails to candidates. Use this tool when you want to:
    - Generate a professional email inviting a candidate to apply
    - Write a job opportunity email based on candidate's background
    Input should be the candidate's background information."""
        )
    )

def create_tools_suite():
    """Creates and configures all available tools."""
    register_default_tools()
    return ToolRegistry.create_all()