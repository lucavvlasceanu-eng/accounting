import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ProtonMail:
    # Kamalesh's code
    __proton_password = os.environ["PROTON_PASSWORD"]
    __proton_mail = os.environ["PROTON_MAIL"]

    def __init__(self):
        pass

    def get_password(self):
        return self.__proton_password

    def login_mail(self):
        logger.info("Initializing ProtonMail login...")

    def create_mail(self, email: str):
        logger.info("Creating email...")
        msg = EmailMessage()
        msg["From"] = self.__proton_mail
        msg["To"] = email
        msg["Subject"] = "Hello"
        msg.set_content("Hello World")
        # TODO send email

    def pull_email(self):
        # TODO pull all the current email
        pass

    def schedule_event(self):
        # TODO schedule an event
        pass

    def apply(self):
        # TODO if a vacancy fufill the role, apply with a tailored resume
        pass


if __name__ == "__main__":
    mail = ProtonMail()

    s = mail.get_password()
    print(s)