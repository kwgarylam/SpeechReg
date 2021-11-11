'''Text to speech by pyttsx3'''
#pip install pyttsx3

import pyttsx3
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# for i, voice in enumerate(voices):
#     print(f"voice[{i}]: {voice.name}")
#     print(f" - {voice.id}")

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)
engine.setProperty('volume', 1)

enText = 'Hello world my friend, I go to school by bus.'
zhText = '你好世界, 我的朋友, 我上學坐巴士'

# Save the text into wav file
engine.save_to_file(enText, 'myAudio.wav')

#engine.say(enText)
engine.runAndWait()


print("Program terminated successfully ...")