from typing import Dict, Type, Union

from .interfaces.base import (
    InputInterface,
    SelectionInterface,
    MessagingInterface,
    ChatInterface,
    UploadInterface
)
from .interfaces.state import StateInterface
from .interfaces.markup import MarkupInterface
from .streamlit_impl.streamlit_renderer import StreamlitRenderer
from .streamlit_impl.state import StreamlitState
from .streamlit_impl.markup import StreamlitMarkup

UIType = Union[
    InputInterface,
    SelectionInterface,
    MessagingInterface,
    ChatInterface,
    UploadInterface
]

class UIFactory:
    """Factory for creating UI components."""
    
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
    
    @classmethod
    def create_ui(cls) -> StreamlitRenderer:
        return StreamlitRenderer()
    
    @classmethod
    def create_state(cls) -> StateInterface:
        return StreamlitState()
    
    @classmethod
    def create_markup(cls) -> MarkupInterface:
        return StreamlitMarkup() 