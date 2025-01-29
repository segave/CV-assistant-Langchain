from typing import Dict, Any

from backend.orchestrator.executor_factory import create_orchestrator


def run_llm(query: str, chat_history: list = None) -> Dict[str, Any]:
    """Run the LLM orchestrator with the given query.

    Args:
        query (str): The user's input query.
        chat_history (list, optional): Previous conversation history. Defaults to None.

    Returns:
        Dict[str, Any]: Response containing the answer and any additional data.
    """
    orchestrator = create_orchestrator()

    response = orchestrator.invoke({"input": query, "chat_history": chat_history})

    return {"answer": response["output"], "context": response.get("context", [])}
