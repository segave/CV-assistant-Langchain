from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.prompts import ChatPromptTemplate
import streamlit as st
from typing import Union, Dict, Any, Optional

EMAIL_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an expert HR professional writing job opportunity emails.
        Write a professional and engaging email to a potential candidate about a job opportunity.
        The email should be:
        - Professional but friendly
        - Highlight relevant matches between the candidate's experience and job requirements
        - Clear and concise
        - Include a call to action
        
        Use the provided information about:
        1. The recruiter (sender)
        2. The job offer
        3. The candidate's background
        
        Format the email with proper structure and spacing."""
    ),
    (
        "user",
        """Write an email using this information:
        
        RECRUITER INFO:
        {recruiter_info}
        
        JOB OFFER:
        Position: {position_title}
        Description: {description}
        Department: {department}
        Location: {location}
        Contract: {contract_type}
        Salary Range: {salary_range}
        Key Requirements:
        {key_requirements}
        Benefits:
        {benefits}
        
        CANDIDATE BACKGROUND:
        {candidate_info}
        """
    ),
])

def create_email_writer_agent():
    """Creates and returns an email writer agent with its executor."""
    
    # Create the LLM
    llm = ChatOpenAI(
        temperature=0.7,
        model=st.session_state.get("selected_model", "gpt-4o-mini")
    )
    
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
    
    # Create the agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=[email_tool],
        verbose=True
    )
    
    return agent_executor

def _generate_email_template(candidate_info: Union[str, Dict[str, Any]], llm: ChatOpenAI) -> str:
    """Internal helper function to generate the base email template."""
    # Extract content if candidate_info is a dictionary
    if isinstance(candidate_info, dict):
        candidate_info = candidate_info.get("page_content", "")

    # Get recruiter information from session state
    recruiter_info = f"""
Name: {st.session_state.get("name", "")}
Position: {st.session_state.get("position", "")}
Company: {st.session_state.get("company", "")}
Email: {st.session_state.get("email", "")}
Phone: {st.session_state.get("phone", "")}
"""
    
    # Generate email content using the provided LLM
    response = llm.invoke(
        EMAIL_PROMPT.format_messages(
            recruiter_info=recruiter_info,
            position_title=st.session_state.get("position_title", ""),
            description=st.session_state.get("description", ""),
            department=st.session_state.get("department", ""),
            location=st.session_state.get("location", ""),
            contract_type=st.session_state.get("contract_type", ""),
            salary_range=st.session_state.get("salary_range", ""),
            key_requirements=st.session_state.get("key_requirements", ""),
            benefits=st.session_state.get("benefits", ""),
            candidate_info=candidate_info,
        )
    )
    
    return response.content

def _personalize_email(template: str, candidate_info: dict) -> str:
    """Internal helper function to personalize the email template."""
    email_content = template
    email_content += f"\n\nBest regards,\n{st.session_state.get('name', '')}"
    return email_content

def write_email(candidate_info: Union[str, Dict[str, Any]]) -> dict:
    """
    Tool that writes a personalized email based on candidate information.
    
    Args:
        candidate_info: String or Dict containing candidate information. Can be:
            - A string with the candidate's background
            - A dict with candidate info from the retriever
            - A dict with name, email and message fields
        llm: Optional ChatOpenAI instance to use for generation
        
    Returns:
        Dictionary with email content and sending data
    """
    # Use provided LLM or create a new one if none provided
    
    llm = ChatOpenAI(
        temperature=0.7,
        model=st.session_state.get("selected_model", "gpt-4o-mini")
    )
    
    # Extract email if candidate_info is a dictionary
    candidate_email = ""
    if isinstance(candidate_info, dict):
        candidate_email = candidate_info.get("metadata", {}).get("email", "")
        candidate_info = candidate_info.get("page_content", "")
    
    # Generate the email content using internal helper functions
    email_content = _generate_email_template(candidate_info, llm)
    final_email = _personalize_email(email_content, candidate_info)
    
    # Prepare email data
    email_data = {
        "to_email": candidate_email,
        "subject": f"Job Opportunity: {st.session_state.get('position_title', '')} at {st.session_state.get('company', '')}",
        "body": final_email,
    }
    
    return {
        "email_content": final_email,
        "email_data": email_data
    } 