import streamlit as st
from streamlit_chat import message
from backend.core import run_llm
from frontend.ui.factory import UIFactory
from frontend.ui.interfaces.base import ChatInterface, MessagingInterface
from frontend.ui.interfaces.state import StateInterface
from frontend.ui.interfaces.markup import MarkupInterface
from typing import Optional, Union


def render_chat_interface(
    ui: Optional[Union[ChatInterface, MessagingInterface]] = None,
    state: Optional[StateInterface] = None,
    markup: Optional[MarkupInterface] = None
):
    """Render the chat interface."""
    ui = ui or UIFactory.create_ui()
    state = state or UIFactory.create_state()
    markup = markup or UIFactory.create_markup()

    # Initialize session state
    state.init_default("chat_answers_history", [])
    state.init_default("user_prompt_history", [])
    state.init_default("chat_history", [])

    markup.markdown("### Chat")

    # Chat container with style
    chat_container = st.container()

    # Input container at the bottom
    input_container = st.container()

    # Display chat history
    with chat_container:
        if state.get("chat_answers_history"):
            for i, (user_query, ai_response) in enumerate(
                zip(
                    state.get("user_prompt_history"),
                    state.get("chat_answers_history"),
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
                    query=user_input, chat_history=state.get("chat_history")
                )

                # Update state
                state.set("user_prompt_history", state.get("user_prompt_history") + [user_input])
                state.set("chat_answers_history", state.get("chat_answers_history") + [response["answer"]])
                state.set("chat_history", state.get("chat_history") + [("human", user_input), ("ai", response["answer"])])

                # Rerun to update chat
                st.rerun()

                ui.success("Response generated!")
