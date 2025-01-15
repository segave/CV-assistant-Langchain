from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain import hub
from backend.tools.retriever import create_flexible_retriever_tool
from backend.tools.help_tool import HelpTool
from backend.agents.email_writer_agent import create_email_writer_agent
from backend.tools.job_matcher import JobMatcherTool
from backend.config import ORCHESTRATOR_INSTRUCTIONS
from backend.tools.email_sender import EmailSenderTool
from langchain.tools import Tool
import streamlit as st


def create_orchestrator():
    """Creates the main orchestrator agent with all available tools."""

    # Load base prompt and add instructions
    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions=ORCHESTRATOR_INSTRUCTIONS)

    # Initialize tools
    tools = [
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

    # Create the agent
    agent = create_react_agent(
        prompt=prompt,
        llm=ChatOpenAI(temperature=0, model=st.session_state.get("selected_model", "gpt-4o-mini")),
        tools=tools,
    )

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        # max_iterations=3
    )
