import json
import Scearch
import VoicePartitions
import SpeechRec
from agent_tools import TOOLS

def listen():
    return SpeechRec.listen_for_speech()


def agent_decide_and_act(user_input):

    SYSTEM_PROMPT = """You are an AI caregiving assistant.

Your job is to decide actions AND extract clean arguments.

Rules:
- Extract only the necessary values
- Remove filler words
- Be precise

Available tools:
- send_message(contact, message)
- clean_storage()
- play_music(song)
- emergency_alert(contact)

If calling a function, respond ONLY in JSON:

{
  "action": "tool_name",
  "args": { }
}

Examples:

User: play some Arijit Singh songs
{
  "action": "play_music",
  "args": { "song": "Arijit Singh songs" }
}

User: send a message to my son that I am not feeling well
{
  "action": "send_message",
  "args": {
    "contact": "son",
    "message": "I am not feeling well"
  }
}
"""
    # Gemini call
    response = Scearch.ask(SYSTEM_PROMPT + "\nUser: " + user_input)
    # Try parsing as JSON (action)
    try:
        data = json.loads(response)

        if "action" in data:
            action = data["action"]
            args = data.get("args", {}) 

            if action in TOOLS:
                result = TOOLS[action](**args)
                return f"{result}"

    except:
        pass

    # fallback → normal response
    return response


def exit():
    VoicePartitions.talk("Goodbye")


def introduce():
    VoicePartitions.talk(
        "Hey this is Violet, your personal assistant powered by Gemini. I can help you and also perform tasks for you."
    )


def clean_command(text):
    text = text.lower()

    filler_words = []

    for i in filler_words:
        text = text.replace(i, "")

    return text