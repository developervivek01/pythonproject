"""DAY 21 OF 100DAYS
 PYTHON PROJECT"""

from gtts import gTTS

text = "Hello everyone this is malwaremint!!"

tts = gTTS(text=text,lang="en")

tts.save("audio.mp3")

print("AUDIO SAVED!!")