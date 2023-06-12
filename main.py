import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = "Daniel Ocampo"
email["to"] = "ocampomary34@gmail.com"
email["subject"] = "University Task"


email.set_content("Dont forget to email your counselor!")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # part of smtp protocol
    smtp.starttls()  # 
    smtp.login("do262431@gmail.com", "dwkxugbmsxziqwwa")
    smtp.send_message(email)
    print("all good boss")