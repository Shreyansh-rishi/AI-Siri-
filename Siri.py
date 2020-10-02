import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening,,")
    speak("I am Siri, Tell me how may i help u")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        speak("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that Again Please...")
        speak("Say that Again Please..")
        return "None"
    return query


if __name__ == "__main__":
    Wishme()
    while True:
        query = takeCommand().lower()
    # For EXecuting Task BAsed on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("According to wikipedia")
            print(results)
            speak(results)

        # elif 'what' in query:
        #     speak("Searching...")
        #     query = query.replace("what", "")
        #     results = webbrowser.open_new("google.com")
        #     results = .summary(query, sentences=5)
        #     speak("The Results are ")
        #     print(result)
        #     speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'what' in query:
            a = webbrowser.open("google.com")
            a.open_new_tab("query")
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\nitac\\Desktop\\Favourites'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codepath  = "C:\\Users\\nitac\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
