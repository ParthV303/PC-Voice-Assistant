import speech_recognition as sr
import pyttsx3
import re

engine = pyttsx3.init()

engine.setProperty('rate', 170)
engine.setProperty('volume', 1)

def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9.,!? ]+', '', text)
    return text

def speak(text):
    try:
        text = re.sub(r"\*\*", "", text)

        text = re.sub(r"\d+\.\s*", "", text)

        text = text.replace("\n", " ")

        text = re.sub(r"\s+", " ", text)

        text = text[:800]

        engine = pyttsx3.init("sapi5")
        engine.setProperty("rate", 170)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except Exception as e:
        print("Speech error:", e)

def listen():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    
    except Exception:
        return ""