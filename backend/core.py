from typing import Dict, Any

from backend.orchestrator.executor_factory import create_orchestrator


def run_llm(query: str, chat_history: list) -> Dict[str, Any]:
    """
    Main entry point for the LLM pipeline.

    Args:
        query: User's input query
        chat_history: List of previous interactions

    Returns:
        Dict containing answer and context
    """
    orchestrator = create_orchestrator()

    response = orchestrator.invoke({"input": query, "chat_history": chat_history})

    return {"answer": response["output"], "context": response.get("context", [])}
