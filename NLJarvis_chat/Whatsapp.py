
import pywhatkit as kt
import datetime
import os
import speech_recognition as sr
from Listen import listen
from speak import Say
from Listen import MicExecution
def send_whatsapp_message():
    try:
        
        Say("What's the recipient's name ?")
        recipient_name = listen().lower()  # Replace with actual contact name
        Say("Recipient Name:"+ recipient_name)
        recipient_number = get_contact_number(recipient_name)
        Say("What's the message content")
        message_content = listen().lower() # Replace with actual message content
        Say("Message Content is :"+message_content)
        # Set the time to send the message (adjust as needed)
        now = datetime.datetime.now()
        hours = now.hour
        minutes = now.minute + 2 # Send the message 1 minute from now

        # Send the WhatsApp message
        kt.sendwhatmsg(recipient_number, message_content, hours, minutes)

        Say(f"WhatsApp message scheduled to be sent at {hours}:{minutes}")
    except Exception as e:
        Say(f"Error: {e}")

def get_contact_number(contact_name):
    # Replace this function with your logic to retrieve the contact number by name
    # You may use a contacts API or a local contacts database
    # For simplicity, let's assume a static mapping in this example
    contacts = {'swayam': '+919004502064', 'kalpesh': '+919321537473','mahindra':'+918623047067'}
    # return contacts.get(contact_name, None)
    contact_number = contacts.get(contact_name.lower())
    if contact_number is None:
        print(f"No contact number found for {contact_name}")
    return contact_number

# Call the function to send the WhatsApp message
# send_whatsapp_message()

