# pip install SpeechRecognition
# https://pypi.org/project/SpeechRecognition/
# pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
# https://www.lfd.uci.edu/~gohlke/pythonlibs/

import speech_recognition as sr
import time

r = sr.Recognizer()

myrecording = False

def readAudioMic():
    # From microphone
    global myrecording

    with sr.Microphone() as source:
        print('Recording... ')
        myrecording = True
        #r.pause_threshold = 0.7
        #r.energy_threshold = 50
        r.dynamic_energy_threshold = False
        audio = r.listen(source, timeout=3, phrase_time_limit=5)


    return audio

def readAudioFile():
    # From audio file
    with sr.AudioFile('audio.mp3') as source:
        audio = r.listen(source)

    return audio

def main():
    try:
        print('------')
        audio = readAudioMic()
        global myrecording

        try:
            result = r.recognize_google(audio, language='yue')
            myrecording = False
            print("Return results: ", result)
            return result
        except sr.UnknownValueError:
            myrecording = False
            print('Unknown Error')
        except LookupError:
            myrecording = False
            print('Could not understand audio')
        except sr.RequestError:
            myrecording = False
            print('Request Error')

    except:
        print('Retry\n------')
        myrecording = False
        #time.sleep(0.1)

if __name__ == '__main__':

    while True:
        main()

    print('Program terminated ...')
