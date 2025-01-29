import streamlit as st
from typing import Any
from .base import UIRenderer

class StreamlitRenderer(UIRenderer):
    """Streamlit implementation of UI renderer."""
    
    def text_input(self, label: str, value: str = "", **kwargs) -> str:
        return st.text_input(label, value=value, **kwargs)
    
    def text_area(self, label: str, value: str = "", height: int = 100, **kwargs) -> str:
        return st.text_area(label, value=value, height=height, **kwargs)
    
    def select_box(self, label: str, options: list, index: int = 0, **kwargs) -> Any:
        return st.selectbox(label, options=options, index=index, **kwargs)
    
    def file_uploader(self, label: str, type: list, **kwargs) -> Any:
        return st.file_uploader(label, type=type, **kwargs)
    
    def success(self, message: str) -> None:
        st.success(message)
    
    def error(self, message: str) -> None:
        st.error(message)
    
    def chat_input(self, placeholder: str, **kwargs) -> str:
        return st.chat_input(placeholder, **kwargs)
    
    def chat_message(self, role: str, **kwargs):
        return st.chat_message(role, **kwargs) 