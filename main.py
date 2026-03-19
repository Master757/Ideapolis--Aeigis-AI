import time
import sys
from Brains import introduce, listen, exit, clean_command, agent_decide_and_act
from VoicePartitions import talk 
from SpeechRec import listen_for_speech
from agent_tools import emergency_alert
import threading
from agent_tools import REMINDERS
import datetime

def reminder_checker():
    #Background thread to monitor reminders.
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        for r in REMINDERS:
            if r["time"] == now and not r["done"]:
                print(f"[ALERT] Reminder: {r['task']}")
                talk(f"Excuse me, I have a reminder for you: {r['task']}")
                r["done"] = True
        time.sleep(10) # Check every 10 seconds

def activate_assistant():
    """
    Once "Hey Violet" is heard, enter command mode.
    """
    talk("Yes?")
    print("...Waiting for your command...")

    while True:
        command = clean_command(listen()).lower()

        if command == "":
            continue

        if command in ["exit", "quit", "goodbye", "stop"]:
            exit()
            return False

        elif command in ["standby", "wait"]:
            talk("Going back to standby.")
            return True

        else:
            print(f"-------->Processing command: {command}")
            try:
                result = agent_decide_and_act(command)
                talk(result)
            except Exception as e:
                talk("I had trouble processing that.")
                print("[Error]: ", e)

def main():
    clock_thread = threading.Thread(target=reminder_checker, daemon=True)
    clock_thread.start()
    introduce()
    while True:
        spoken_text = listen_for_speech().lower()
        if spoken_text == "":
            continue

        if spoken_text in ["exit", "quit", "goodbye", "stop", "bye bye"]:
            exit() #attribute to 'Brains'
            return False
        if "help me" in spoken_text or "send emergency msg" in spoken_text:
            print("Emergency words detected...")
            emergency_alert("son")

        if "hey violet" in spoken_text:
            print(" Activated")
            should_continue = activate_assistant()
            if not should_continue:
                break

        


        time.sleep(0.5)
    sys.exit()

if __name__ == "__main__":
    main()
