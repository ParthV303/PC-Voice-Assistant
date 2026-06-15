import subprocess
import os
import webbrowser


def open_app(command):

    if "chrome" in command:
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        return "Opening Chrome"

    elif "notepad" in command:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad"
    
    elif "whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening whatsapp"

    return None


def shutdown():
    os.system("shutdown /s /t 1")