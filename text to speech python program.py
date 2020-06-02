from gtts import gTTS
from playsound import playsound
import os

words = 'Hi, I am the text to speech assistent and ' \
         'Aryan Singh is the administrator here. '


language = 'en'

obey = gTTS(text=words, lang=language, slow=False)


obey.save("audio.mp3")

os.system("audio.mp3")

#ANOTHER METHOD
#audio = 'speech.mp3'
#language = 'en'


#sp = gTTs(text = "I want to learn programming",
#          lang = language, slow = False)

#sp.save("audio")
#playsound("audio")