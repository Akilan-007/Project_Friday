import speech_recognition as sr
import pyttsx3
import smtplib
import datetime
import pywhatkit
import wikipedia
import pyjokes
import os
import time
import webbrowser
import pyaudio

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('hi.......i am friday..... what can i do for u')
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening')
            talk('waiting for your command')
            listener.adjust_for_ambient_noise(source, 0.5)
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')
            print(command)
    except:
        pass
    return command

def runfriday():

    command = take_command()

    if 'who are you' in command or 'name' in command or 'yourself' in command:
        print('I am Friday. A voice assistant, created by Mr.Akilan.')
        talk('I am Friday. A voice assistant, created by Mr.Akilan.')

    elif 'hello' in command or 'hai' in command or 'hi' in command:
        talk('hi....')

    elif 'play' in command:
        command = command.replace('play','')
        print('playing ',command )
        pywhatkit.playonyt(command)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Now the time is ' + time)

    elif 'date' in command:
        date = datetime.datetime.now().date()
        print(date)
        talk(date)

    elif 'who is ' in command:
        name = command.replace('who is','')
        detail = wikipedia.summary(name,2)
        print(detail)
        talk(detail)

    elif 'tell me about ' in command:
        name = command.replace('tell me about ','')
        detail = wikipedia.summary(name,2)
        print(detail)
        talk(detail)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'search' in command.lower():
        ind = command.lower().split().index('search')
        search = command.split()[ind + 1:]
        webbrowser.open(
            "https://www.google.com/search?q="+"+".join(search)
        )
        talk('searching in google chrome')

    elif 'open' in command:
        balance = command.replace('open','')
        command = balance.lower()
        if 'chrome' in command:
            talk('opening google chrome')
            os.startfile(
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"    
            )
        elif 'vs code' in command or 'visual studio code' in command:
            talk('opening visual studio code')
            os.startfile(
                r"C:\Users\pc\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            )
        elif 'word' in command:
            talk('opening word document')
            os.startfile(
                r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            )
        elif 'youtube' in command:
            talk('opening Youtube')
            webbrowser.open('https://www.youtube.com/')

while True:
    runfriday()
    break
