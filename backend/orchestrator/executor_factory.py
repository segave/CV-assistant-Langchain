from langchain.agents import AgentExecutor
from .agent_factory import create_agent
from .tools_manager import create_tools_suite

def create_orchestrator():
    """Creates the orchestrator with its executor."""
    agent = create_agent()
    tools = create_tools_suite()

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
    ) 