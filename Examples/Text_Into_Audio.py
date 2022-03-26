from gtts import gTTS
# pip install gtts
from playsound import playsound
# pip install playsound
audio = 'speech.mp3'
language = 'en'
sp = gTTS(text = """enter your text which u want to
          convert into audio file""",
          lang= language, slow=False)
sp.save(audio)
playsound (audio)