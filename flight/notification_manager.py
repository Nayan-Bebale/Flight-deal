import smtplib
from twilio.rest import Client
from data_manager import DataManager
from email.mime.text import MIMEText

from dotenv import load_dotenv
import os

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")

My_EMAIL = os.getenv("My_EMAIL")
PASSWORD = os.getenv("PASSWORD")
dm = DataManager()


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, message):

        for email in dm.get_user_data():
            subject = "Flight Price Alert"
            msg = MIMEText(message, "plain", "utf-8")
            msg["Subject"] = subject
            msg["From"] = My_EMAIL
            msg["To"] = email

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=My_EMAIL, password=PASSWORD)
                connection.send_message(msg)
            # print(email)


# no = NotificationManager()
# send_email()