import os

def find_and_open_file(filename, search_path="C:\\"):

    for root, dirs, files in os.walk(search_path):
        
        for file in files:

            if filename.lower() in file.lower():

                file_path = os.path.join(root, file)

                os.startfile(file_path)

                return f"Opening {file}"

    return "File not found"