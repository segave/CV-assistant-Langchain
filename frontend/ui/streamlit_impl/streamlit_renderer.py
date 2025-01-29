import streamlit as st
from typing import Any

from ..interfaces.base import (
    InputInterface,
    SelectionInterface,
    MessagingInterface,
    ChatInterface,
    UploadInterface
)

class StreamlitRenderer(
    InputInterface,
    SelectionInterface,
    MessagingInterface,
    ChatInterface,
    UploadInterface
):
    """Streamlit implementation of all UI interfaces."""
    
    # Input methods
    def text_input(self, label: str, value: str = "", **kwargs) -> str:
        return st.text_input(label, value=value, **kwargs)
    
    def text_area(self, label: str, value: str = "", **kwargs) -> str:
        return st.text_area(label, value=value, **kwargs)
    
    # Selection methods
    def select_box(self, label: str, options: list, **kwargs) -> Any:
        return st.selectbox(label, options=options, **kwargs)
    
    # Messaging methods
    def success(self, message: str) -> None:
        st.success(message)
    
    def error(self, message: str) -> None:
        st.error(message)
    
    # Chat methods
    def chat_input(self, placeholder: str, **kwargs) -> str:
        return st.chat_input(placeholder, **kwargs)
    
    def chat_message(self, role: str, **kwargs):
        return st.chat_message(role, **kwargs)
    
    # Upload methods
    def file_uploader(self, label: str, type: list, **kwargs) -> Any:
        return st.file_uploader(label, type=type, **kwargs)