from abc import ABC, abstractmethod
from typing import Any

class StateInterface(ABC):
    """Interface for application state management."""
    
    @abstractmethod
    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from state."""
        pass
    
    @abstractmethod
    def set(self, key: str, value: Any) -> None:
        """Set a value in state."""
        pass
    
    @abstractmethod
    def init_default(self, key: str, default: Any) -> None:
        """Initialize a key with default value if not exists."""
        pass 