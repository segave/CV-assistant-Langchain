import streamlit as st
from frontend.ui.factory import UIFactory
from frontend.ui.base import UIRenderer


def render_profile(ui: UIRenderer = None):
    """Render user profile with style"""
    ui = ui or UIFactory.create()

    # Initialize session state for user profile
    if "name" not in st.session_state:
        st.session_state["name"] = ""
    if "position" not in st.session_state:
        st.session_state["position"] = ""
    if "company" not in st.session_state:
        st.session_state["company"] = ""
    if "email" not in st.session_state:
        st.session_state["email"] = ""
    if "phone" not in st.session_state:
        st.session_state["phone"] = ""

    st.markdown("### Profile")
    st.session_state["name"] = ui.text_input("Name", value=st.session_state["name"])
    st.session_state["position"] = ui.text_input("Position", value=st.session_state["position"])
    st.session_state["company"] = ui.text_input("Company", value=st.session_state["company"])
    st.session_state["email"] = ui.text_input("Email", value=st.session_state["email"])
    st.session_state["phone"] = ui.text_input("Phone", value=st.session_state["phone"])
