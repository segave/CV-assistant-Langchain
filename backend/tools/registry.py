from typing import Callable, Dict, List
from langchain.tools import BaseTool

class ToolRegistry:
    """Registry for managing tool registration and creation."""
    
    _tools: Dict[str, Callable[[], BaseTool]] = {}
    
    @classmethod
    def register(cls, name: str, tool_creator: Callable[[], BaseTool]) -> None:
        """Register a new tool creator function."""
        cls._tools[name] = tool_creator
    
    @classmethod
    def create_all(cls) -> List[BaseTool]:
        """Create instances of all registered tools."""
        return [creator() for creator in cls._tools.values()]
    
    @classmethod
    def clear(cls) -> None:
        """Clear all registered tools."""
        cls._tools.clear()