import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import sys
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def anser(ques):
    ques = ques.lower()
    if 'wikipedia' in ques:
        query = ques.replace("wikipedia","")
        if query == 0:
            speak("Are you trying to search something?")
            speak("please try again.")
            anser(takeCommand())
        speak("Searching wikipedia...")
        print(query)
        try:
            results = wikipedia.summary(query, sentences = 5, auto_suggest = False)
            print(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Diambigous keyword, pls specify...")
            anser(takeCommand())
        except wikipedia.exceptions.PageError as e1:
            speak("Wanna try that again? ")
            anser(takeCommand())
        speak("According to Wikipedia")
        speak(results)
    elif 'open youtube' in ques:
        webbrowser.open("youtube.com")
    elif 'stop listening' in ques:
        speak("Sure Sir.")

    speak("May I help you with anything else, Sir? ")
    ques = takeCommand()
    if ques == 'no':
        anser(ques)
    else:
        speak("Have a good day Sir!! ")
        sys.exit()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            audio1 = r.recognize_google(audio, language='en-in')
            print("User said: \n", audio1)
            return audio1
        except Exception as e:
            print("Please say that again..\n")


if __name__ == '__main__':
    speak("Hello Sir, How may I help you?")
    reply = takeCommand()
    if reply:
        anser(reply)
    else:
        speak("Let me know when you need something...")