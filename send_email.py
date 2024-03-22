import smtplib
import ssl
import os
from dotenv import load_dotenv
load_dotenv("environment.env")


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("Sender_Email")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("Receiver_Email")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
