import streamlit as st

def render_model_selector():
    """Render the AI model selector."""
    # Available models
    models = {
        "GPT-4o": "gpt-4o",
        "GPT-4o-mini": "gpt-4o-mini",
    }
    
    # Initialize session state for model selection
    if "selected_model" not in st.session_state:
        st.session_state["selected_model"] = "gpt-4o-mini"
    
    # Create the model selector
    selected_model_name = st.selectbox(
        "Select AI Model",
        options=list(models.keys()),
        index=list(models.keys()).index(
            next(k for k, v in models.items() if v == st.session_state["selected_model"])
        )
    )
    
    # Update the session state with the selected model
    st.session_state["selected_model"] = models[selected_model_name] 