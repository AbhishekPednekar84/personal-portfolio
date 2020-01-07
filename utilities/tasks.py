import os
import smtplib
import ssl
from email.message import EmailMessage
from celery_app import create_celery_app

celery = create_celery_app()


@celery.task
def send_email(caller_name, caller_email, caller_subject, caller_message):
    """
    Method to send an email based on the details provided on the contact me page

    Parameters
    ----------
    caller_name: name of the individual contacting me
    caller_email: email of the individual contacting me
    caller_subject: email subject provided by the individual
    caller_message: email message provided by the individual
    """
    sender_email = os.getenv("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")
    recipient_email = os.getenv("RECIPIENT_EMAIL")
    port = 465
    smtp_server = "smtp.gmail.com"

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = caller_subject
    msg.set_content(
        f"Email from {caller_name} ({caller_email})\n\n{caller_message}"
    )

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(sender_email, password)
        smtp.send_message(msg)
