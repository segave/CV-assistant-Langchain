import streamlit as st
from streamlit_chat import message
from backend.core import run_llm
from frontend.ui.factory import UIFactory
from frontend.ui.interfaces.base import ChatInterface, MessagingInterface
from typing import Union


def render_chat_interface(ui: Union[ChatInterface, MessagingInterface] = None):
    """Render the chat interface."""
    ui = ui or UIFactory.create()

    st.markdown("### Chat")

    # Initialize session state
    if "chat_answers_history" not in st.session_state:
        st.session_state["chat_answers_history"] = []
        st.session_state["user_prompt_history"] = []
        st.session_state["chat_history"] = []
        st.session_state["current_input"] = ""

    # Chat container with style
    chat_container = st.container()

    # Input container at the bottom
    input_container = st.container()

    # Display chat history
    with chat_container:
        if st.session_state["chat_answers_history"]:
            for i, (user_query, ai_response) in enumerate(
                zip(
                    st.session_state["user_prompt_history"],
                    st.session_state["chat_answers_history"],
                )
            ):
                message(user_query, is_user=True, key=f"user_msg_{i}")
                message(ai_response, key=f"assistant_msg_{i}")

    # Input area
    with input_container:
        st.write("")  # Spacing
        col1, col2 = st.columns([4, 1])

        with col1:
            user_input = ui.text_input(
                label="Message",
                label_visibility="collapsed",
                placeholder="Type your question here...",
                key="input_field",
            )

        with col2:
            submit_button = st.button("Send", use_container_width=True)

        if submit_button and user_input:
            with st.spinner("Generating response..."):
                # Process input
                response = run_llm(
                    query=user_input, chat_history=st.session_state["chat_history"]
                )

                # Update state
                st.session_state["user_prompt_history"].append(user_input)
                st.session_state["chat_answers_history"].append(response["answer"])
                st.session_state["chat_history"].append(("human", user_input))
                st.session_state["chat_history"].append(("ai", response["answer"]))

                # Rerun to update chat
                st.rerun()

                ui.success("Response generated!")
