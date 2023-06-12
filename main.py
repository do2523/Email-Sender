import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = "Daniel Ocampo"
email["to"] = "ocampomary34@gmail.com"
email["subject"] = "You Won 1,000,000 dollars!"


email.set_content("I am a Python Maser!")