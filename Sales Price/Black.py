import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import smtplib
import pywhatkit as kit


print("inializing Black...")
MASTER = "IPUL"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[1].id)

#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#function
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour < 12 :
        speak("Good Morning " + MASTER)
    elif hour >= 12 and hour < 18 :
        speak("Good Afternoon " + MASTER)
    else:
        speak("Good Evening " + MASTER)
        speak("")    


#Microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening....")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"User said : {query}\n")

    except Exception as e:
        print("say that again please...")
        query = ''

    return query



#main start here
speak('Hello My Name is Black, I can Help You Ipul..?')
wishMe()   

def run_black():
    query = takeCommand()   

    #logic for tasks as per query

    #wikipedia
    if "wikipedia" in query.lower() :
        print("Searching wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)

        #youtube
    elif "open youtube" in query.lower() :
        print("Open Youtube...")
        url = "youtube.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)

    #google
    elif "open google" in query.lower() :
        print("Open google...")
        url = "google.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)

    #email
    elif "open email" in query.lower() :
        print("Open email...")
        url = "gmail.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url) 

    #whatsapp
    elif "open whatsapp" in query.lower() :
        print("Open whatsapp...")
        url = "web.whatsapp.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url) 

    #music
    elif "play music" in query.lower() :
        print("play music...")
        songs_dir  = "D:\\My Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[0]))

    #play youtube
    elif "play" in query.lower() :
        song = query.replace('play','')
        print('play' + song)
        speak('play' + song)
        kit.playonyt(song)

    #time
    elif "time" in query.lower() :
        strTime = datetime.datetime.now().strftime("%I:%M:%p")
        speak(f"{MASTER} time is {strTime}")
    
    else:
        speak('')

while True:
    run_black()
