import speech_recognition
import pyttsx3
import requests
import urllib.request

from bs4 import BeautifulSoup
from playsound import playsound
from gtts import gTTS

import os


engine = pyttsx3.init() 



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
                text = text.replace('define ', '')
                url='https://www.vocabulary.com/dictionary/' + text
                htmlfile = urllib.request.urlopen(url)
                soup = BeautifulSoup(htmlfile, 'lxml')              
                soup1 = soup.find(class_="short")
                soup1 = soup1.get_text()
                print(soup1)
                engine.say(soup1) 
                engine.runAndWait()

                
            elif text == "how is your day going":
                engine.say("Good! Thanks for asking.")
                engine.runAndWait()
            else:
                print(text)
                print("Invalid command...")
            
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue
