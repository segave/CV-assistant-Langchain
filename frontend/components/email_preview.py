from typing import Optional

from frontend.ui.factory import UIFactory
from frontend.ui.interfaces.base import InputInterface
from frontend.ui.interfaces.state import StateInterface
from frontend.ui.interfaces.markup import MarkupInterface
from backend.tools.email_sender.tool import EmailSenderTool


def render_email_preview(
    ui: Optional[InputInterface] = None,
    state: Optional[StateInterface] = None,
    markup: Optional[MarkupInterface] = None
):
    """Render the email preview section.
    
    Displays generated emails and provides options to edit and send them.
    
    Args:
        ui: UI renderer instance
        state: State management instance
        markup: Markup renderer instance
    """
    ui = ui or UIFactory.create_ui()
    state = state or UIFactory.create_state()
    markup = markup or UIFactory.create_markup()

    markup.markdown("### Generated Emails")

    # Initialize email history in state if not exists
    state.init_default("email_history", [])
    state.init_default("editing_email_index", None)
    
    # Get email history
    email_history = state.get("email_history", [])
    
    if not email_history:
        markup.markdown("No emails have been generated yet.")
        return

    # Check if we're editing an email
    editing_index = state.get("editing_email_index")
    if editing_index is not None:
        email = email_history[editing_index]
        
        markup.markdown("### Edit Email")
        
        # Edit form
        new_to = ui.text_input("To:", value=email.get("to_email", ""))
        new_subject = ui.text_input("Subject:", value=email.get("subject", ""))
        new_body = ui.text_area("Content:", value=email.get("body", ""), height=200)
        
        col1, col2 = markup.columns([1, 1])
        with col1:
            if ui.button("Save Changes"):
                # Update email in history
                email_history[editing_index] = {
                    "to_email": new_to,
                    "subject": new_subject,
                    "body": new_body
                }
                state.set("email_history", email_history)
                state.set("editing_email_index", None)
        
        with col2:
            if ui.button("Cancel"):
                state.set("editing_email_index", None)
        
        return

    # Display each email in the history
    for i, email in enumerate(email_history):
        with ui.expander(f"Email to: {email.get('to_email', 'No recipient')} - {email.get('subject', 'No subject')}"):
            # Email details
            markup.markdown("**To:** " + email.get('to_email', 'No recipient'))
            markup.markdown("**Subject:** " + email.get('subject', 'No subject'))
            markup.markdown("**Content:**")
            markup.markdown(email.get('body', 'No content'))
            
            # Action buttons
            col1, col2 = markup.columns([1, 1])
            with col1:
                if ui.button("Edit", key=f"edit_email_{i}"):
                    state.set("editing_email_index", i)
            
            with col2:
                if ui.button("Send", key=f"send_email_{i}"):
                    try:
                        # Use EmailSenderTool to send the email
                        email_sender = EmailSenderTool()
                        result = email_sender._run({
                            "email_data": {
                                "to_email": email.get("to_email"),
                                "subject": email.get("subject"),
                                "body": email.get("body")
                            }
                        })
                        
                        if "Error" in result:
                            raise Exception(result)
                        
                        #ui.success(f"Email sent successfully to {email.get('to_email')}")
                        
                        # Remove sent email from history
                        email_history.pop(i)
                        state.set("email_history", email_history)
                        
                    except Exception as e:
                        ui.error(f"Failed to send email: {str(e)}")