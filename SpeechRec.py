import speech_recognition as sr

def listen_for_speech():
    recog = sr.Recognizer()
    mic = sr.Microphone()

    print(" ~~ Listening...")

    with mic as source:
        try:
            recog.adjust_for_ambient_noise(source, duration=0.5)
            audio = recog.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("XXXXXXXXXX No speech detected. XXXXXXXXXXXX")
            return ""

    try:
        text = recog.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Couldn't understand that")
        return ""
    except sr.RequestError:
        print("Google API unavailable")
        return "[offline]"
    
