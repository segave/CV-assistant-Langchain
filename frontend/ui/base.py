from abc import ABC, abstractmethod
from typing import Any, Optional, Dict

class UIRenderer(ABC):
    """Abstract base class for UI renderers."""
    
    @abstractmethod
    def text_input(self, label: str, value: str = "", **kwargs) -> str:
        """Render a text input field."""
        pass
    
    @abstractmethod
    def text_area(self, label: str, value: str = "", height: int = 100, **kwargs) -> str:
        """Render a text area field."""
        pass
    
    @abstractmethod
    def select_box(self, label: str, options: list, index: int = 0, **kwargs) -> Any:
        """Render a select/dropdown box."""
        pass
    
    @abstractmethod
    def file_uploader(self, label: str, type: list, **kwargs) -> Any:
        """Render a file upload component."""
        pass
    
    @abstractmethod
    def success(self, message: str) -> None:
        """Display a success message."""
        pass
    
    @abstractmethod
    def error(self, message: str) -> None:
        """Display an error message."""
        pass
    
    @abstractmethod
    def chat_input(self, placeholder: str, **kwargs) -> str:
        """Render a chat input field."""
        pass
    
    @abstractmethod
    def chat_message(self, role: str, **kwargs):
        """Render a chat message."""
        pass 