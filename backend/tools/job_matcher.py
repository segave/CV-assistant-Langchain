from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from backend.agents.retriever import create_flexible_retriever_tool
from typing import Dict, Any, Union
from pydantic import Field
import streamlit as st

class JobMatcherTool(BaseTool):
    name: str = "job_matcher"
    description: str = """Finds candidates that match the current job opening requirements. Use this tool when you want to:
    - Find candidates that match the job requirements
    - Search for potential candidates for the position
    - Get a list of suitable candidates based on skills and experience
    No input is needed, it will use the current job description.
    """

    llm: ChatOpenAI = Field(
        default_factory=lambda: ChatOpenAI(
            temperature=0, 
            model=st.session_state.get("selected_model", "gpt-4o-mini")
        )
    )
    retriever: BaseTool = Field(default_factory=create_flexible_retriever_tool)

    def _run(self, query: str = "") -> str:
        """
        Searches for candidates that match the job requirements.

        Returns:
            String containing analysis of matching candidates
        """
        # Build search query from job requirements
        search_query = f"""
Position: {st.session_state.get('position_title', '')}

Description:
{st.session_state.get('description', '')}

Department: {st.session_state.get('department', '')}
Location: {st.session_state.get('location', '')}
Contract: {st.session_state.get('contract_type', '')}
Salary Range: {st.session_state.get('salary_range', '')}

Key Requirements:
{st.session_state.get('key_requirements', '')}

Benefits:
{st.session_state.get('benefits', '')}
"""

        # Search candidates using the retriever's function directly
        candidates_info = self.retriever.func({"input": search_query, "search_type": "general"})

        # Create prompt for analyzing matches
        analysis_prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """You are an expert HR recruiter analyzing candidate matches for a job position.
                Compare the candidates' profiles with the job requirements and provide a detailed analysis.
                Focus on:
                1. Overall match percentage
                2. Key matching skills and experience
                3. Potential areas for growth
                4. Recommendations
                
                Format your response clearly and concisely."""
            ),
            (
                "user",
                """Analyze these candidates for the following position:
                
                JOB REQUIREMENTS:
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
                
                CANDIDATES INFORMATION:
                {candidates_info}
                
                Provide a detailed analysis focusing on the match between each candidate's profile 
                and our specific job requirements. Include a match percentage for each candidate."""
            ),
        ])

        # Generate analysis
        response = self.llm.invoke(
            analysis_prompt.format_messages(
                position_title=st.session_state.get('position_title', ''),
                description=st.session_state.get('description', ''),
                department=st.session_state.get('department', ''),
                location=st.session_state.get('location', ''),
                contract_type=st.session_state.get('contract_type', ''),
                salary_range=st.session_state.get('salary_range', ''),
                key_requirements=st.session_state.get('key_requirements', ''),
                benefits=st.session_state.get('benefits', ''),
                candidates_info=candidates_info,
            )
        )

        return response.content

    async def _arun(self, query: str) -> Any:
        """Async implementation"""
        raise NotImplementedError("This tool doesn't support async execution")
