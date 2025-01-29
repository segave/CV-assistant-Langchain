import streamlit as st
from frontend.ui.factory import UIFactory
from frontend.ui.interfaces.base import InputInterface
from frontend.ui.interfaces.state import StateInterface
from frontend.ui.interfaces.markup import MarkupInterface
from typing import Optional

def render_job_description(
    ui: Optional[InputInterface] = None,
    state: Optional[StateInterface] = None,
    markup: Optional[MarkupInterface] = None
):
    """Render the job description input section."""
    ui = ui or UIFactory.create_ui()
    state = state or UIFactory.create_state()
    markup = markup or UIFactory.create_markup()
    
    # Initialize session state for job description fields
    state.init_default("position_title", "")
    state.init_default("description", "")
    state.init_default("department", "")
    state.init_default("location", "")
    state.init_default("contract_type", "")
    state.init_default("salary_range", "")
    state.init_default("key_requirements", "")
    state.init_default("benefits", "")

    markup.markdown("### Job Description")

    state.set("position_title", ui.text_input("Position Title", value=state.get("position_title")))
    state.set("description", ui.text_area("Description", value=state.get("description"), height=200))
    state.set("department", ui.text_input("Department", value=state.get("department")))
    state.set("location", ui.text_input("Location", value=state.get("location")))
    state.set("contract_type", ui.text_input("Contract Type", value=state.get("contract_type")))
    state.set("salary_range", ui.text_input("Salary Range", value=state.get("salary_range")))
    state.set("key_requirements", ui.text_area("Key Requirements", value=state.get("key_requirements"), height=150))
    state.set("benefits", ui.text_area("Benefits", value=state.get("benefits"), height=150)) 