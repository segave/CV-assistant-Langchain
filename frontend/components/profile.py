import streamlit as st
from frontend.ui.factory import UIFactory
from frontend.ui.interfaces.base import InputInterface
from frontend.ui.interfaces.state import StateInterface
from frontend.ui.interfaces.markup import MarkupInterface
from typing import Optional


def render_profile(
    ui: Optional[InputInterface] = None,
    state: Optional[StateInterface] = None,
    markup: Optional[MarkupInterface] = None
):
    """Render user profile with style"""
    ui = ui or UIFactory.create_ui()
    state = state or UIFactory.create_state()
    markup = markup or UIFactory.create_markup()

    # Initialize session state for user profile
    state.init_default("name", "")
    state.init_default("position", "")
    state.init_default("company", "")
    state.init_default("email", "")
    state.init_default("phone", "")

    markup.markdown("### Profile")
    state.set("name", ui.text_input("Name", value=state.get("name")))
    state.set("position", ui.text_input("Position", value=state.get("position")))
    state.set("company", ui.text_input("Company", value=state.get("company")))
    state.set("email", ui.text_input("Email", value=state.get("email")))
    state.set("phone", ui.text_input("Phone", value=state.get("phone")))
