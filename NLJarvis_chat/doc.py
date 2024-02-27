import os
import time
import speech_recognition as sr
import pyautogui
from Listen import listen

def Note():
    os.system("start winword")
    time.sleep(2)  # Wait for Word to open

    # Simulate keyboard shortcuts to create a new document
    pyautogui.hotkey('ctrl', 'n')
    pyautogui.hotkey('esc')

    while True:
        command = listen()
        if "exit" in command:
            break
        else:
            # Type the dictated content
            pyautogui.typewrite(command)

if __name__ == "__main__":
    Note()
