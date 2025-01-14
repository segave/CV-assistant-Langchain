from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from typing import Dict, Any, Union
from pydantic import Field
import streamlit as st

class EmailWriterTool(BaseTool):
    name: str = "email_writer"
    description: str = """Writes personalized job opportunity emails to candidates. Use this tool when you want to:
    - Generate a professional email inviting a candidate to apply
    - Write a job opportunity email based on candidate's background
    Input should be the candidate's background information.
    """

    llm: ChatOpenAI = Field(
        default_factory=lambda: ChatOpenAI(
            temperature=0.7, 
            model=st.session_state.get("selected_model", "gpt-4o-mini")
        )
    )
    prompt: ChatPromptTemplate = Field(
        default_factory=lambda: ChatPromptTemplate.from_messages(
            [
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
        
        Format the email with proper structure and spacing.""",
                ),
                (
                    "user",
                    """Write an email using this information:
        
        RECRUITER INFO:
        {recruiter_info}
        
        JOB OFFER:
        Position: {position_title}
        description: {description}
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
        """,
                ),
            ]
        )
    )

    def _run(self, candidate_info: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generates and optionally sends a professional email to a candidate.

        Args:
            candidate_info: String or Dict containing candidate's information

        Returns:
            Dictionary with email content and sending data
        """
        # Extract email if candidate_info is a dictionary
        candidate_email = ""
        if isinstance(candidate_info, dict):
            candidate_email = candidate_info.get("metadata", {}).get("email", "")
            candidate_info = candidate_info.get("page_content", "")

        # Get recruiter information from session state
        recruiter_info = f"""
Name: {st.session_state.get("name", "")}
Position: {st.session_state.get("position", "")}
Company: {st.session_state.get("company", "")}
Email: {st.session_state.get("email", "")}
Phone: {st.session_state.get("phone", "")}
"""

        # Get job description fields from session state
        position_title = st.session_state.get("position_title", "")
        description = st.session_state.get("description", "")
        department = st.session_state.get("department", "")
        location = st.session_state.get("location", "")
        contract_type = st.session_state.get("contract_type", "")
        salary_range = st.session_state.get("salary_range", "")
        key_requirements = st.session_state.get("key_requirements", "")
        benefits = st.session_state.get("benefits", "")

        # Generate email content
        response = self.llm.invoke(
            self.prompt.format_messages(
                recruiter_info=recruiter_info,
                position_title=position_title,
                description=description,
                department=department,
                location=location,
                contract_type=contract_type,
                salary_range=salary_range,
                key_requirements=key_requirements,
                benefits=benefits,
                candidate_info=candidate_info,
            )
        )

        # Format final email with signature
        email_content = response.content
        email_content += f"\n\nBest regards,\n{st.session_state.get('name', '')}"

        # Prepare email data
        email_data = {
            "to_email": candidate_email,
            "subject": f"Job Opportunity: {position_title} at {st.session_state.get('company', '')}",
            "body": email_content,
        }

        # Return both the email content and the data for sending
        return {"email_content": email_content, "email_data": email_data}

    async def _arun(self, query: str) -> Any:
        """Async implementation"""
        raise NotImplementedError("This tool doesn't support async execution")
