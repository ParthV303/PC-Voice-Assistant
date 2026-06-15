import webbrowser
import os
import psutil


def search_web(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)


def search_youtube(query):
    url = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(url)


def close_app(app_name):
    os.system(f"taskkill /f /im {app_name}.exe")


def create_folder(name):
    os.makedirs(name, exist_ok=True)


def get_cpu_usage():
    return psutil.cpu_percent()


def handle_smart_command(command):

    command = command.lower()

    if "close" in command:
        app = command.replace("close", "").strip()
        close_app(app)
        return f"Closing {app}"

    elif "search" in command:
        query = command.replace("search", "").strip()
        search_web(query)
        return "Searching the web"

    elif "youtube" in command:
        query = command.replace("youtube", "").strip()
        search_youtube(query)
        return "Opening YouTube"

    elif "create folder" in command:
        folder = command.replace("create folder", "").strip()
        create_folder(folder)
        return "Folder created"

    elif "cpu usage" in command:
        cpu = get_cpu_usage()
        return f"CPU usage is {cpu} percent"

    return None