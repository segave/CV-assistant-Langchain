import streamlit as st

from frontend.components.profile import render_profile
from frontend.components.chat import render_chat_interface
from frontend.components.email_credentials import render_email_credentials
from frontend.components.job_description import render_job_description
from frontend.components.document_uploader import render_document_uploader
from frontend.components.model_selector import render_model_selector
from frontend.styles.apply_styles import apply_custom_styles
from frontend.ui.factory import UIFactory

# Page configuration MUST be the first Streamlit command
st.set_page_config(
    page_title="CV Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    """Main application entry point."""
    ui = UIFactory.create()

    # Apply custom styling after page config
    apply_custom_styles()

    # Render model selector at the top
    render_model_selector(ui)

    # Create three columns: left sidebar, main content, right sidebar
    left_sidebar, main_content, right_sidebar = st.columns([1, 2, 1])

    # Left sidebar with tabs
    with left_sidebar:
        tabs = st.tabs(["User Profile", "Job Description", "Email Credentials"])
        
        with tabs[0]:
            render_profile(ui)
        
        with tabs[1]:
            render_job_description(ui)
        
        with tabs[2]:
            render_email_credentials(ui)

    # Main content
    with main_content:
        st.header("CV Assistant")
        render_chat_interface(ui)

    # Right sidebar for document upload
    with right_sidebar:
        render_document_uploader(ui)

if __name__ == "__main__":
    main()