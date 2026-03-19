import pywhatkit
import pyautogui
import time

import datetime

# Store reminders in a simple list
# Format: {"task": "Take medicine", "time": "20:30"}
REMINDERS = []

def set_reminder(task, time_at):
    """
    time_at should be in HH:MM format (24-hour)
    Example: set_reminder("Take heart medicine", "10:30")
    """
    try:
        datetime.datetime.strptime(time_at, "%H:%M")
        REMINDERS.append({"task": task, "time": time_at, "done": False})
        print(f"[REMINDER SET] {task} at {time_at}")
        return f"Okay, I've set a reminder to {task} at {time_at}."
    except ValueError:
        return "I couldn't understand the time format. Please use HH:MM."


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
    "emergency_alert": emergency_alert,
    "set_reminder": set_reminder
}

CONTACTS = {
    "brother": "+91943308727",
    "son": "+918653432900"
}
