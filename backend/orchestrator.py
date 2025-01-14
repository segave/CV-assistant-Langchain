from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain import hub
from backend.agents.retriever import create_flexible_retriever_tool
from backend.tools.help_tool import HelpTool
from backend.agents.email_writer import EmailWriterTool
from backend.agents.job_matcher import JobMatcherTool
from backend.config import ORCHESTRATOR_INSTRUCTIONS
from backend.tools.email_sender import EmailSenderTool
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
        EmailWriterTool(),
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
