from ai_brain import ask_ai
from speech_engine import listen, speak
from wake_word import is_wake_word_detected, remove_wake_word

while True:
    print("Waiting for wake word...")

    text = listen()

    if not text:
        continue

    if is_wake_word_detected(text):

        print("Wake word detected!")
        speak("Yes sir, I am listening.")

        print("Listening for command...")
        command = listen()

        if not command:
            continue

        if command.lower() == "exit":
            speak("Goodbye sir.")
            break

        response = ask_ai(command)
        response = response[:600] 
        print("Jarvis:", response)
        speak(response)