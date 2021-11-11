# pip install SpeechRecognition
# https://pypi.org/project/SpeechRecognition/
# pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
# https://www.lfd.uci.edu/~gohlke/pythonlibs/

import speech_recognition as sr
import time

r = sr.Recognizer()

def readAudioMic():
    # From microphone
    with sr.Microphone() as source:
        print('Recording... ')
        #r.pause_threshold = 0.7
        #r.energy_threshold = 500
        r.dynamic_energy_threshold = False
        audio = r.listen(source, timeout=3, phrase_time_limit=5)

    return audio

def readAudioFile():
    # From audio file
    with sr.AudioFile('audio.mp3') as source:
        audio = r.listen(source)

    return audio

while True:

    try:
        print('------')
        audio = readAudioMic()

        try:
            print("Result: \n" + r.recognize_google(audio, language='yue'))
        except sr.UnknownValueError:
            print('Unknown Error')
        except LookupError:
            print('Could not understand audio')
        except sr.RequestError:
            print('Request Error')

    except:
        print('Retry\n------')
        time.sleep(0.5)

print('Program terminated ...')
