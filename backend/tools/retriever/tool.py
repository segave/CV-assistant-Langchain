from langchain.tools import Tool
from typing import Dict, Any

from .config import get_search_config
from .input_processor import process_input
from .search_chain import create_search_chain

def create_flexible_retriever_tool(temperature: float = 0, k: int = 4):
    """Creates a flexible retriever tool."""
    search_config = get_search_config(temperature, k)
    
    def flexible_func(input_data: Dict[str, Any] | str) -> Dict[str, Any]:
        processed_input = process_input(input_data)
        search_chain = create_search_chain(
            processed_input["search_type"],
            search_config
        )
        
        try:
            result = search_chain.invoke({
                "input": processed_input["query"],
                "chat_history": processed_input["chat_history"]
            })
            return result
        except Exception as e:
            return {"answer": f"Error during retrieval: {str(e)}"}

    return Tool(
        name="Flexible_CV_Retriever",
        func=flexible_func,
        description="""Search through a CV database to retrieve candidates based on criteria like skills, names, or general information.
        
        **Input Format**:
        - String: Treated as a general search query.
        - Dictionary: 
          - "input" (required): The search query string.
          - "search_type" (optional): One of ["skills", "name", "general"]. Defaults to "general".
          - "chat_history" (optional): List of previous interactions for additional context.
        
        **Examples**:
        1. Search by skills: {"input": "Python and AWS experience", "search_type": "skills"}
        2. Search by name: {"input": "John Smith", "search_type": "name"}
        3. General search: {"input": "Candidates with startup experience"}
        
        **Output**: Returns relevant CV information matching the criteria.""",
    ) 