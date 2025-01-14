import streamlit as st
from PIL import Image
import requests
from io import BytesIO


def get_profile_picture(email: str) -> Image:
    """Get avatar from Gravatar or a placeholder"""
    try:
        gravatar_url = (
            f"https://www.gravatar.com/avatar/{hash(email)}?d=identicon&s=200"
        )
        response = requests.get(gravatar_url)
        return Image.open(BytesIO(response.content))
    except:
        return None


def render_profile():
    """Render user profile with style"""
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

    with st.container():
        # Header
        st.markdown(
            "<h2 style='text-align: center;'>Profile</h2>", unsafe_allow_html=True
        )

        # User information
        col1, col2 = st.columns([1, 2])

        with col1:
            profile_pic = get_profile_picture(st.session_state["email"])
            if profile_pic:
                st.image(profile_pic, width=100)

        with col2:
            st.markdown("### User Information")
            st.session_state["name"] = st.text_input("Name", value=st.session_state["name"])
            st.session_state["position"] = st.text_input("Position", value=st.session_state["position"])
            st.session_state["company"] = st.text_input("Company", value=st.session_state["company"])
            st.session_state["email"] = st.text_input("Email", value=st.session_state["email"])
            st.session_state["phone"] = st.text_input("Phone", value=st.session_state["phone"])
