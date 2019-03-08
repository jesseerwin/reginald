import speech_recognition as sr
import wthr as w
import textsay as ts
r = sr.Recognizer()
mic = sr.Microphone()

# listen for speech and send to google's speech service
def send():
    try:
        print("Speak!")
        with mic as source:
            audio = r.listen(source)
        print("Sending to google..")
        global transcript
        transcript = r.recognize_google(audio)
        print("Output: " + transcript)
    except:
        print("Unintelligible speech")
        send()

# check for commands and run them
while True:
    send()
    if "Reginald" in transcript:
        if "weather" in transcript:
            ts.texttospeech(w.printstatus()) 
        elif "stop" in transcript:
            print("Stopping")
            raise SystemExit(0)
    else:
        print("Nothing to do") 
