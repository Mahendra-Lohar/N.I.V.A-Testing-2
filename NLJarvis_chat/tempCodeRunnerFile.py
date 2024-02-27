
# def recognize_speech():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#     try:
#         command = recognizer.recognize_google(audio)
#         print("You said:", command)
#         return command
#     except sr.UnknownValueError:
#         print("Sorry, could not understand the audio.")
#         return None
