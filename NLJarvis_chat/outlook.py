# Email drafting:

import os
import speech_recognition as sr
from Listen import listen
import smtplib
from speak import Say
from Listen import MicExecution
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'smtp_username': 'your email',
    'smtp_password': 'your password',
}

def send_email(subject, body, to_email):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("your email","your password")
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail("your email", to_email, message)
    server.quit()


def verify_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False
def main():
    Say("Hello, How can I assist you with your email?")
    
    Say("What is the subject of the email?")
    subject = listen()

    Say("What should be the body of the email?")
    body = listen()
    while True:
        Say("To whom should I send the email?")
        id = listen() + "@gmail.com"
        to_email=''.join(id.split())
        if verify_email(to_email):
            Say(to_email)
            Say("Is this the correct email address? Say send it  or no.")
            confirmation = listen()
            Say(confirmation)
            if confirmation == "send it":
                send_email(subject, body, to_email)
                Say("Email sent successfully.")
                break
        else:
            Say("The email address you provided is invalid. Would you like to provide the email address again? Say yes or no.")
            confirmation = listen()
            if confirmation != "yes":
                break


if __name__ == "__main__":
    main()
