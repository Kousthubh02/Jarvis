import datetime
import speech_recognition as sr
import pyttsx3
import pyaudio
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("I am jarvis . I am at your service Mr. Stark")


def takeCommand():
    '''
    this function takes command from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        r.energy_threshold=100
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"
    return query



if __name__ =="__main__":
    wishMe()
    while (True):
        query = takeCommand().lower()
    # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" sir, the time is {strTime}")

        elif 'open code' in query:
            codepath ="C:\\Users\\kaust\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'quit' in query:
            exit()





