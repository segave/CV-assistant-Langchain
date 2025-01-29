import streamlit as st
from frontend.ui.factory import UIFactory
from frontend.ui.base import UIRenderer

def render_job_description(ui: UIRenderer = None):
    """Render the job description input section."""
    ui = ui or UIFactory.create()  # Default to Streamlit if no renderer provided
    
    # Initialize session state for job description fields
    if "position_title" not in st.session_state:
        st.session_state["position_title"] = ""
    if "description" not in st.session_state:
        st.session_state["description"] = ""
    if "department" not in st.session_state:
        st.session_state["department"] = ""
    if "location" not in st.session_state:
        st.session_state["location"] = ""
    if "contract_type" not in st.session_state:
        st.session_state["contract_type"] = ""
    if "salary_range" not in st.session_state:
        st.session_state["salary_range"] = ""
    if "key_requirements" not in st.session_state:
        st.session_state["key_requirements"] = ""
    if "benefits" not in st.session_state:
        st.session_state["benefits"] = ""

    st.markdown("### Job Description")

    st.session_state["position_title"] = ui.text_input("Position Title", value=st.session_state["position_title"])
    st.session_state["description"] = ui.text_area("Description", value=st.session_state["description"], height=200)
    st.session_state["department"] = ui.text_input("Department", value=st.session_state["department"])
    st.session_state["location"] = ui.text_input("Location", value=st.session_state["location"])
    st.session_state["contract_type"] = ui.text_input("Contract Type", value=st.session_state["contract_type"])
    st.session_state["salary_range"] = ui.text_input("Salary Range", value=st.session_state["salary_range"])
    st.session_state["key_requirements"] = ui.text_area("Key Requirements", value=st.session_state["key_requirements"], height=150)
    st.session_state["benefits"] = ui.text_area("Benefits", value=st.session_state["benefits"], height=150) 