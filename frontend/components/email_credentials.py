import streamlit as st

def render_email_credentials():
    """Render the email credentials input section."""
    # Initialize session state for email credentials
    if "email" not in st.session_state:
        st.session_state["email"] = ""
    if "password" not in st.session_state:
        st.session_state["password"] = ""

    st.markdown("### Email Credentials")
    email = st.text_input("Enter your email address:", value=st.session_state["email"])
    password = st.text_input("Enter your email password:", type="password", value=st.session_state["password"])

    # Store credentials in session state
    st.session_state["email"] = email
    st.session_state["password"] = password 