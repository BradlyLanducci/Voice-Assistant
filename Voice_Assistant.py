import speech_recognition
import pyttsx3
import requests
import urllib.request
import os

from bs4 import BeautifulSoup
from playsound import playsound
from gtts import gTTS

def main():      
    engine = pyttsx3.init() 

    recognizer = speech_recognition.Recognizer()

    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()

                words = text.split(" ")

                if "define" in text:
                        try:
                            print("Defining...")
                            text = text.replace('define ', '')
                            url='https://www.vocabulary.com/dictionary/' + text
                            htmlfile = urllib.request.urlopen(url)
                            soup = BeautifulSoup(htmlfile, 'lxml')              
                            soup1 = soup.find(class_="short")
                            soup1 = soup1.get_text()
                            engine.say(soup1) 
                            engine.runAndWait()
                        except:
                            engine.say("Define command failed. Say, define and then say a word...")
                            engine.runAndWait()
                            
                elif text == "how is your day going":
                    engine.say("Good! Thanks for asking.")
                    engine.runAndWait()
                    
                elif "multiply" in text:
                    num1 = int(words[1])
                    num2 = int(words[3])
                    try: 
                        answer = num1 * num2
                        engine.say(answer)
                        engine.runAndWait()
                    except:
                        engine.say("To multiply... say multiply, x times y.")
                        engine.runAndWait()
                elif "divide" in text:
                    num1 = int(words[1])
                    num2 = int(words[3])
                    try: 
                        answer = num1 / num2
                        engine.say(answer)
                        engine.runAndWait()
                    except:
                        engine.say("To multiply... say multiply, x times y.")
                        engine.runAndWait()
                elif "add" in text:
                    num1 = int(words[1])
                    num2 = int(words[3])
                    try: 
                        answer = num1 + num2
                        engine.say(answer)
                        engine.runAndWait()
                    except:
                        engine.say("To multiply... say multiply, x times y.")
                        engine.runAndWait()
                elif "subtract" in text:
                    num1 = int(words[1])
                    num2 = int(words[3])
                    try: 
                        answer = num1 - num2
                        engine.say(answer)
                        engine.runAndWait()
                    except:
                        engine.say("To multiply... say multiply, x times y.")
                        engine.runAndWait()
                else:
                    engine.say(f"Command {text} doesn't exist.")
                    engine.runAndWait()
                
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue

if __name__ == "__main__":
    main()
