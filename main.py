import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # Another option would be using the OS module 

html =Template( Path("index.html").read_text())
email = EmailMessage()
email['from'] = "Daniel Ocampo"
email["to"] = "ocampomary34@gmail.com"
email["subject"] = "Urgent Message"


email.set_content(html.substitute({"name":"Daniel"}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # part of smtp protocol
    smtp.starttls()  # 
    smtp.login("do262431@gmail.com", "dwkxugbmsxziqwwa")
    smtp.send_message(email)
    print("all good boss")