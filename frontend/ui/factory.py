from typing import Dict, Type
from .base import UIRenderer
from .streamlit_renderer import StreamlitRenderer

class UIFactory:
    """Factory for creating UI renderers."""
    
    _renderers: Dict[str, Type[UIRenderer]] = {
        "streamlit": StreamlitRenderer
    }
    
    @classmethod
    def register_renderer(cls, name: str, renderer_class: Type[UIRenderer]) -> None:
        """Register a new UI renderer."""
        cls._renderers[name] = renderer_class
    
    @classmethod
    def create(cls, renderer_type: str = "streamlit") -> UIRenderer:
        """Create a UI renderer instance."""
        if renderer_type not in cls._renderers:
            raise ValueError(f"Unknown renderer type: {renderer_type}")
        
        return cls._renderers[renderer_type]() 