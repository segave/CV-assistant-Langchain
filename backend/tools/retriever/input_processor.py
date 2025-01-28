from typing import Dict, Any
import json

def process_input(input_data: Dict[str, Any] | str) -> Dict[str, Any]:
    """Processes and validates input data."""
    if isinstance(input_data, str):
        try:
            input_data = json.loads(input_data)
        except json.JSONDecodeError:
            input_data = {
                "input": input_data,
                "search_type": "general",
                "chat_history": [],
            }

    return {
        "search_type": input_data.get("search_type", "general"),
        "query": input_data.get("input", input_data if isinstance(input_data, str) else ""),
        "chat_history": input_data.get("chat_history", [])
    } 