from dotenv import load_dotenv
import os

load_dotenv(override=True)

INDEX_NAME = os.environ["INDEX_NAME"]
NAMESPACE = os.environ["NAMESPACE"]

def get_search_config(temperature: float = 0, k: int = 4):
    """Returns search configuration parameters."""
    return {
        "llm_config": {
            "temperature": temperature
        },
        "search_kwargs": {
            "k": k
        }
    } 