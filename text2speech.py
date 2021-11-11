'''Text to speech by gtts'''
#pip install gtts pygame

import gtts
import pygame
import sys

enText = 'Hello world my friend, I go to school by bus.'
zhText = '你好世界, 我的朋友, 我上學坐巴士'

#print(gtts.lang.tts_langs()) # Check the supporting language

#tts = gtts.gTTS(enText) #English text
tts = gtts.gTTS(zhText, lang='zh-tw') # Chinese text

# Save the text into mp3 file
filename = 'audio.mp3'
#tts.save(filename)

# Playback the audio file
pygame.mixer.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()
while True:
    if pygame.mixer.get_init(): #if the mixer is already initialized
        if pygame.mixer.music.get_busy(): #if the mixer is playing the audio file
            pass
        else:
            break
            #sys.exit(0)

print("Program terminated successfully ...")