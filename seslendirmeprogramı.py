
import os
from gtts import gTTS
import playsound2
x=input('seslendirmek istediğiniz yazıyı yapıştırın: ')
from gtts.lang import tts_langs
tts = gTTS(x,lang='tr')
tts.save('hello.mp3')
os.system('hello.mp3')
#os.remove("hello.mp3")
