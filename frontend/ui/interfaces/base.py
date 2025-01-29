from abc import ABC, abstractmethod
from typing import Any

class InputInterface(ABC):
    @abstractmethod
    def text_input(self, label: str, value: str = "", **kwargs) -> str:
        pass
    
    @abstractmethod
    def text_area(self, label: str, value: str = "", **kwargs) -> str:
        pass

class SelectionInterface(ABC):
    @abstractmethod
    def select_box(self, label: str, options: list, **kwargs) -> Any:
        pass

class MessagingInterface(ABC):
    @abstractmethod
    def success(self, message: str) -> None:
        pass
    
    @abstractmethod
    def error(self, message: str) -> None:
        pass

class ChatInterface(ABC):
    @abstractmethod
    def chat_input(self, placeholder: str, **kwargs) -> str:
        pass
    
    @abstractmethod
    def chat_message(self, role: str, **kwargs):
        pass

class UploadInterface(ABC):
    @abstractmethod
    def file_uploader(self, label: str, type: list, **kwargs) -> Any:
        pass 