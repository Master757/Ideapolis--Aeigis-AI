import pywhatkit
import pyautogui
import time

def send_message(contact, message):
    if not contact or not message:
        return "Missing contact or message"

    contact = contact.lower()

    if contact in CONTACTS:
        number = CONTACTS[contact]
    else:
        return f"Contact '{contact}' not found"

    print(f"Sending '{message}' to {contact} -> {number}")
    pywhatkit.sendwhatmsg_instantly(number, message)
    time.sleep(6)
    pyautogui.press("enter")
    return f"Message sent to {contact}"

def clean_storage():
    print("Cleaning storage...")
    return "Storage cleaned"

def play_music(song):
    print(f" playing music called with: {song}")
    pywhatkit.playonyt(song)
    return f"Playing {song}"

def emergency_alert(contact="brother"):
    contact = contact.lower()
    if contact in CONTACTS:
        number = CONTACTS[contact]
    else:
        return "Emergency contact not found"

    print("[ACTION] Emergency alert triggered")
    pywhatkit.sendwhatmsg_instantly(number,"Emergency detected. Please check immediately."
    )
    time.sleep(6)
    pyautogui.press("enter")
    return "Emergency alert sent"

TOOLS = {
    "send_message": send_message,
    "clean_storage": clean_storage,
    "play_music": play_music,
    "emergency_alert": emergency_alert
}

CONTACTS = {
    "brother": "+91943308727",
    "son": "+918653432900"
}