WAKE_WORD = "chintu"

def is_wake_word_detected(text):
    if not text:
        return False

    text = text.lower().strip()

    print("DEBUG - Checking:", text)  
    return WAKE_WORD in text

def remove_wake_word(text):
    text = text.lower().strip()
    return text.replace(WAKE_WORD, "").strip()