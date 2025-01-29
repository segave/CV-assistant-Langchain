from typing import Dict, Type, Union
from .interfaces.base import (
    InputInterface,
    SelectionInterface,
    MessagingInterface,
    ChatInterface,
    UploadInterface
)
from .streamlit_renderer import StreamlitRenderer

UIType = Union[
    InputInterface,
    SelectionInterface,
    MessagingInterface,
    ChatInterface,
    UploadInterface
]

class UIFactory:
    """Factory for creating UI renderers."""
    
    _renderers: Dict[str, Type[UIType]] = {
        "streamlit": StreamlitRenderer
    }
    
    @classmethod
    def register_renderer(cls, name: str, renderer_class: Type[UIType]) -> None:
        """Register a new UI renderer."""
        cls._renderers[name] = renderer_class
    
    @classmethod
    def create(cls, renderer_type: str = "streamlit") -> UIType:
        """Create a UI renderer instance."""
        if renderer_type not in cls._renderers:
            raise ValueError(f"Unknown renderer type: {renderer_type}")
        
        return cls._renderers[renderer_type]() 