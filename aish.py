import pyttsx3
import datetime
import wikipedia
import webbrowser
import io
import os
import sys
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def wish():
    currentDT = int(datetime.datetime.now().hour)
    if currentDT>=00 and currentDT<12:
        speak("good morning")
    elif currentDT>=12 and currentDT<17:
            speak("good afternoon")
    elif currentDT>=17 and currentDT<21:
            speak("good Evening")
    else:
        speak("good night")

    speak("I am Your Personal Voice assistant ")
    #speak("What can i do for you")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Listning...")
                r.non_speaking_duration=0.080
                audio = r.listen(source)
        try:
            print("recognisnig..")
            query =r.recognize_google(audio,language="en-in") 
            return query
        except Exception as e:
            print(e)          
    


if __name__ == "__main__": 
    wish()
    speak("here are the some things you can try")
    print("search in wikipedia (example:salman khan wikipedia)")
    print("open youtube")
    print("open google")
    print("open stack overflow")
    print("to quit say exit")
    speak("search in wikipedia example salman khan wikipedia")
    speak("open youtube")
    speak("open google")
    speak("open stack overflow") 
    speak("to quit say exit")      
    while(True):
            speak("what should I do")
            query = takecommand()
            query=query.lower()
            print(query)
            if "wikipedia" in query:
                speak("searching in wikipedia")
                query=query.replace("wikipedia" ,"")
                results = wikipedia.summary(query , sentences=3)
                print(results)
                speak("according to wikipedia ")
                speak(results)
            elif "youtube" in query:
                speak("opening youtube")
                result = "www.youtube.com"
                webbrowser.open(result)
            elif "google" in query:
                speak("opening google")
                result = "www.google.com"
                webbrowser.open(result)
            elif "stack overflow" in query:
                speak("opening stack overflow")
                result = "www.stackoverflow.com"
                webbrowser.open(result)
            elif "time" in query:
                currentDT = datetime.datetime.now().time()
                speak("current time and date is")
                speak(currentDT)   
            elif "exit" in query:
                speak("Thank you")    
                break     
            else: 
                speak("here are the some things you can try")
                print("search in wikipedia")
                print("open youtube")
                print("open google")
                print("open stack overflow")
                speak("search in wikipedia")
                speak("open youtube")
                speak("open google")
                speak("open stack overflow")
           