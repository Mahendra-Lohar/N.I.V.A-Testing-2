# #Hindi or English -command
# # English command

# # requires libarary 1) googletrans

# # import speech_recognition as sr
# # from googletrans import Translator

# # 1 listen function :Hinid to English


import speech_recognition as sr
from googletrans import Translator


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 4)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
    except:
        return ""
    query = str(query)
    return query.lower()


def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"you :{data}.")
    # print(f"you : {data}.")
    return data


def MicExecution():
    query = listen()
    data = TranslationHinToEng(query)
    return data


MicExecution()


# import speech_recognition as sr
# from googletrans import Translator

# def listen():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source, timeout=10)
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language="hi-IN")
#         print(f"You said: {query}")
#     except Exception as e:
#         print(f"Error: {str(e)}")
#         return ""
#     query = str(query)
#     return query.lower()

# def TranslationHinToEng(text):
#     translate = Translator()
#     result = translate.translate(text, dest="en")
#     data = result.text
#     print(f"Translation: {data}")
#     return data

# def MicExecution():
#     query = listen()
#     data = TranslationHinToEng(query)
#     return data

# MicExecution()
