from speech_engine import listen, speak
from ai_brain import ask_ai
from automation import open_app, shutdown
from file_search import find_and_open_file
from memory import save_history, get_history
from smart_control import handle_smart_command

def main():

    speak("stif Activated")

    while True:

        print("Listening for wake word...")
        text = listen()

        if not text:
            continue

        text = text.lower()

        # Wake word detection
        if "stif" in text:

            speak("Yes sir")

            print("Listening for command...")
            command = listen()

            if not command:
                continue

            command = command.lower()

            print("Command:", command)

            # smart control
            result = handle_smart_command(command)

            if result:
                speak(result)
                continue

            # System Automation
            response = open_app(command)

            if response:
                speak(response)
                continue

            elif "shutdown" in command:
                speak("Shutting down system")
                shutdown()
                continue

            # file seaching

            elif "find" in command or "search file" in command:
                filename = command.replace("find", "").replace("search file", "").strip()
                result = find_and_open_file(filename)
                speak(result)
                continue

            # history

            elif "show history" in command:
                history = get_history()

                if history:
                     speak("Here is your recent history")

                     for row in history[-5:]:
                         query = row[0]
                         response = row[1]

                         speak(f"you asked {query}")
                         speak(f"I answered {response}")
                    
                else:
                    speak("No history found")  
                    continue 

            # personality
            
            elif "thank you" in command:
                speak("You're welcome sir. Always happy to help.") 
                continue    

            elif "good job" in command:
                speak("Thank you sir.") 
                continue

            elif "who are you" in command:
                speak("I am stif, your personal artificial intelligence assistant.") 
                continue
            
            elif "stop stif" in command or "exit stif" in command or "bye" in command:
                speak("Goodbye sir") 
                break

            else:
                answer = ask_ai(command)
                save_history(command, answer)
                speak(answer)


if __name__ == "__main__":
    main()