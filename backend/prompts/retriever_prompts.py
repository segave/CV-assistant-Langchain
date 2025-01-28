from langchain.prompts import ChatPromptTemplate

SEARCH_PROMPTS = {
    "skills": ChatPromptTemplate.from_template(
        """Given the chat history: {chat_history}
        And the user's question: {input}
        Rephrase the question to find candidates with specific technical skills. 
        Focus on programming languages, tools, and technical expertise.
        In your response, always include:
        1. The name of the candidate (from metadata["name"])
        2. The specific skills they have
        3. Any relevant context about their experience"""
    ),
    "name": ChatPromptTemplate.from_template(
        """Given the chat history: {chat_history}
        And the user's question: {input}
        Rephrase the question to search for candidates by their name.
        In your response, include:
        1. The candidate's full name (from metadata["name"])
        2. Key information found about them"""
    ),
    "general": ChatPromptTemplate.from_template(
        """Given the chat history: {chat_history}
        And the user's question: {input}
        Search for relevant information in the CVs.
        Always include the candidate's name (from metadata["name"]) in your response."""
    ),
} 