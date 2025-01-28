from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from .llm_config import create_orchestrator_llm
from .tools_manager import create_tools_suite
from backend.config import ORCHESTRATOR_INSTRUCTIONS

def create_agent():
    """Creates the main agent with its tools and configuration."""
    # Load base prompt and add instructions
    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions=ORCHESTRATOR_INSTRUCTIONS)

    # Get tools and LLM
    tools = create_tools_suite()
    llm = create_orchestrator_llm()

    # Create the agent
    agent = create_react_agent(
        prompt=prompt,
        llm=llm,
        tools=tools,
    )

    return agent 