import os
import smtplib
import ssl
from email.message import EmailMessage


def send_email(caller_name, caller_email, caller_subject, caller_message):
    sender_email = os.environ.get('EMAIL_USER')
    recipient_email = 'abhi_ap@hotmail.com'
    password = os.environ.get('EMAIL_PASS')
    port = 465
    smtp_server = 'smtp.gmail.com'

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = caller_subject
    msg.set_content(
        f'Email from {caller_name} ({caller_email})\n\n{caller_message}')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(sender_email, password)
        smtp.send_message(msg)
