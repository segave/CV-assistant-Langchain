from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool

from .tool import write_email
from .llm_config import create_email_llm

def create_email_writer_agent():
    """Create and configure an email writer agent.
    
    Creates an agent specialized in writing professional emails to job candidates,
    configured with specific tools and prompts for email composition.
    
    Returns:
        AgentExecutor: Configured agent executor ready to write emails.
    """
    
    # Create the LLM
    llm = create_email_llm()
    
    # Create the email writing tool
    email_tool = Tool(
        name="write_email",
        func=write_email,
        description="""Writes and formats a professional email to a candidate about a job opportunity. 
Use this tool when you want to write an email to a candidate.
Input should be the candidate's information (either as a string or a dictionary containing their background and experience).
The tool will automatically use the job description and recruiter information from the current session.
Returns a dictionary with the email content and sending data."""
    )
    
    # Create the agent with specific instructions
    prompt = hub.pull("langchain-ai/react-agent-template").partial(
        instructions="""You are an AI assistant that helps write professional emails to job candidates.
        When given candidate information, use the write_email tool to generate a personalized email.
        The tool will use the job description and recruiter information from the current session.
        Always pass the candidate information directly to the write_email tool."""
    )
    
    # Create the agent
    agent = create_react_agent(
        llm=llm,
        tools=[email_tool],
        prompt=prompt
    )
    
    return AgentExecutor(
        agent=agent,
        tools=[email_tool],
        verbose=True
    ) 