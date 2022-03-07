import speech_recognition
import pyttsx3
import requests
import urllib.request

from bs4 import BeautifulSoup
from playsound import playsound
from gtts import gTTS

import os

recognizer = speech_recognition.Recognizer()

while True:

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            voice = text

            if "define" in text:
                
                print("Defining...")
                
                url='https://www.vocabulary.com/dictionary/' + text
                htmlfile = urllib.request.urlopen(url)
                soup = BeautifulSoup(htmlfile, 'lxml')              
                soup1 = soup.find(class_="short")
                soup1 = soup1.get_text()
                print(soup1)


                
            elif text == "how is your day going":
                print("Good! Thanks for asking.")
            else:
                print("Invalid command...")
            
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue


# Functionality to have it talk back, currently only works by creating a file
# The main issue with this is it needs to create a new file everytime.


##            language = 'en'
##
##            myobj = gTTS(text=voice, lang=language, slow=False)
##
##            myobj.save("welcome.mp3")
##  
##            # Playing the converted file
##            playsound('C:/Users/bradl/Desktop/Code Projects/Speech_Recognition/Voice-Assistant/welcome.mp3')
##            print(f"Recognized {text}")
