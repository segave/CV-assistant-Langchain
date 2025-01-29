from langchain.tools import BaseTool
from typing import Any

from .query_builder import build_search_query
from .analyzer import analyze_candidates
from backend.tools.retriever import create_flexible_retriever_tool

class JobMatcherTool(BaseTool):
    name: str = "job_matcher"
    description: str = """Finds candidates that match the current job opening requirements. Use this tool when you want to:
    - Find candidates that match the job requirements
    - Search for potential candidates for the position
    - Get a list of suitable candidates based on skills and experience
    No input is needed, it will use the current job description.
    """

    def _run(self, query: str = "") -> str:
        """Searches for candidates that match the job requirements."""
        # Build search query
        search_query = build_search_query()
        
        # Get retriever and search candidates
        retriever = create_flexible_retriever_tool()
        candidates_info = retriever.func({"input": search_query, "search_type": "general"})
        
        # Analyze matches
        return analyze_candidates(candidates_info)

    async def _arun(self, query: str) -> Any:
        """Async implementation"""
        raise NotImplementedError("This tool doesn't support async execution") 