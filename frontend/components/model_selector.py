import streamlit as st
from frontend.ui.factory import UIFactory
from frontend.ui.interfaces.base import SelectionInterface

def render_model_selector(ui: SelectionInterface = None):
    """Render the AI model selector."""
    ui = ui or UIFactory.create()
    
    # Crear columnas para centrar y reducir el ancho del selector
    _, col2, _ = st.columns([3, 2, 3])
    
    # Available models
    models = {
        "GPT-4o": "gpt-4o",
        "GPT-4o-mini": "gpt-4o-mini",
    }
    
    # Initialize session state for model selection
    if "selected_model" not in st.session_state:
        st.session_state["selected_model"] = "gpt-4o-mini"
    
    with col2:
        # Create the model selector
        selected_model_name = ui.select_box(
            "Select AI Model",
            options=list(models.keys()),
            index=list(models.keys()).index(
                next(k for k, v in models.items() if v == st.session_state["selected_model"])
            )
        )
    
    # Update the session state with the selected model
    st.session_state["selected_model"] = models[selected_model_name] 