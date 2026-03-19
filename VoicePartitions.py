import platform

if platform.system() == "Windows":
    import win32com.client
    import pythoncom
    import keyboard
    import time

    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    def stop():
        speaker.Skip("Sentence", 99999999)
        pythoncom.CoUninitialize()

    def speak(text):
        pythoncom.CoInitialize()
        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        print("---------->>>>> Speaking started...")
        speaker.Speak(text, 1)  # async

        try:
            while True:
                if speaker.Status.RunningState == 1:
                    break
                if keyboard.is_pressed('q'):#for debug termninal checks
                    stop()
                    break
                time.sleep(0.05)
        except Exception as e:
            print(f"[Error during speech] {e}")

        pythoncom.CoUninitialize()

    def talk(text):
        print("Assistant says:", text)
        speak(text)
        print("---- Speech End ----\n")

else:
    #No voice in linux [applicability throuhg docker]
    def talk(text):
        print("Assistant says:", text)