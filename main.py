import time
import sys
from Brains import introduce, listen, exit, clean_command, agent_decide_and_act
from VoicePartitions import talk 
from SpeechRec import listen_for_speech
from agent_tools import emergency_alert

introduce()

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
    while True:
        spoken_text = listen_for_speech().lower()

        if spoken_text == "":
            continue

        if spoken_text in ["exit", "quit", "goodbye", "stop", "bye bye"]:
            exit() #attribute to 'Brains'
            return False
        
        if "hey violet" in spoken_text:
            print(" Activated")
            should_continue = activate_assistant()
            if not should_continue:
                break

        if "help" in spoken_text:
            print("Emergency words detected...")
            emergency_alert()


        time.sleep(0.5)
    sys.exit()

if __name__ == "__main__":
    main()