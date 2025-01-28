from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict

def create_email_message(sender_email: str, email_data: Dict) -> MIMEMultipart:
    """Creates the email message with proper formatting."""
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email_data['to_email']
    msg['Subject'] = email_data['subject']
    msg.attach(MIMEText(email_data['body'], 'plain'))
    return msg 