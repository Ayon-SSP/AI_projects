import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Hi!I'm Cortana")

MASTER = "Ayon..........."

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# speak function will pronounce the string which is pass to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


# This function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    speak("Hi!I'm Cortana. How may I help you?")


# Thish function will take comand from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ayoniiiiiiii10@gmail.com', 'P@$$ay04')
    server.sendmail("ayoniiiiii10@gmail.com", to, content)
    server.close()


# Main program starts hear...
# speak("Initializing Cortana...")
wishMe()
query = takeCommand()

# Logic for executing tasks as per the query
if 'wikipedia' in query.lower():
    speak('searching wikipesea...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    # webbrowser.open("youtube.com")
    url = "youtube.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    print("opening youtube for You.....")

elif 'open google' in query.lower():
    # webbrowser.open("google.com")
    url = "google.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open my blog' in query.lower():
    # webbrowser.open("google.com")
    url = "https://www.google.com/search?q=karmakaraayon&sxsrf=ALeKk00zBkTefnqO8-dqFl6NtAVmd32-nA%3A1621777972093&ei=NF6qYOGoBbPjz7sP3c-SeA&oq=karmakaraa&gs_lcp=Cgdnd3Mtd2l6EAMYADIECCMQJzIECCMQJzIECAAQDTIECAAQDTIECAAQDTIGCAAQDRAKMgYIABANEAoyBAgAEA0yBggAEA0QCjIGCAAQDRAeOgcIABCwAxANOgUILhCRAjoFCC4QsQM6AgguOggILhCxAxCDAToFCAAQkQI6CAgAELEDEIMBOggIABCxAxCRAjoFCAAQsQM6AggAOggILhDHARCvAToECAAQCjoECAAQHlCKE1jXImC9LmgDcAB4AYAB1ASIAZAZkgELMC4zLjUuMS4wLjKYAQCgAQGqAQdnd3Mtd2l6yAEBwAEB&sclient=gws-wiz"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'my photos from google' in query.lower():
    # webbrowser.open("google.com")
    url = "https://www.google.com/search?q=karmakaraayon&sxsrf=ALeKk02mPmg0nbbSucfv4PIId_gI07Wfaw:1621777979834&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiXvpHj-d_wAhUlieYKHVUNC1UQ_AUoA3oECAEQBQ&biw=1707&bih=844&dpr=1.13"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'my profile' in query.lower():
    # webbrowser.open("google.com")
    url = "https://www.linkedin.com/in/ayon-k/"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open reddit' in query.lower():
    # webbrowser.open("google.com")
    url = "reddit.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    songs_dir = "C:\\Users\\admin\\Music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))

elif 'pdf' in query.lower():
    url = "file:///E:/PC%20thinges%20in%20this/books/PythonNotesForProfessionals%20(1)%20(1)%20(1)%20(1)%20(2)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).pdf"
    webbrowser.open_new(url)

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}....................Come on..................... hurry up")

elif 'open code' in query.lower():
    codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
    os.startfile(codePath)
    print("VS CODE in ayon's pc")

elif 'email to iron' in query.lower():
    try:
        speak("What should I send")
        content = takeCommand()
        to = "ayoniiiiii10@gmail.com"
        sendEmail(to, content)
        speak("Email has sent successfully")
    except Exception as e:
        print(e)
        speak("Sorry my friend Ayon......... I am not able to send this email")
