# ... (previous code)
from win10toast import ToastNotifier
import time
import speech_recognition as sr
import pyttsx3

notifications = []

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        return query.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

# Define the speak function
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ... (the rest of your code)


def set_notification(title, message, time_in_seconds):
    toaster = ToastNotifier()
    time.sleep(time_in_seconds)
    toaster.show_toast(title, message, duration=10)

def read_notifications():
    if notifications:
        speak("Here are your notifications:")
        for i, notification in enumerate(notifications, start=1):
            speak(f"Notification {i}: {notification[0]}")
            speak(f"Message: {notification[1]}")
        speak("End of notifications.")
    else:
        speak("You have no notifications.")

if __name__ == "__main__":
    while True:
        command = listen()
        if "exit" in command:
            break
        elif "set notification" in command:
            speak("What is the title of your notification?")
            notification_title = listen()
            speak("What is the message for your notification?")
            notification_message = listen()
            speak("In how many seconds should the notification appear?")
            try:
                time_in_seconds = 10
                set_notification(notification_title, notification_message, time_in_seconds)
                speak(f"Notification '{notification_title}' set to appear in {time_in_seconds} seconds.")
            except ValueError:
                speak("Invalid time. Please specify the time in seconds.")

        elif "read notifications" in command:
            speak("Reading notifications.")
            read_notifications()
            # You can implement code here to read the notifications from a storage or database.

        # Add more commands and functionalities as needed.

