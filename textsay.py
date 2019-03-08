from gtts import gTTS
import os
def texttospeech(speech): 
    tts = gTTS(text=speech, lang='en')
    tts.save("audio.mp3")
    os.system("mpv audio.mp3")
