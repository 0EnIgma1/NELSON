import pyttsx3 as pyt
import speech_recognition as sr
import datetime as dt
import os
import wikipedia
import webbrowser
import pywhatkit
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import random

engine = pyt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def joke():
    myjokes = ["bored of being bored because being bored is boring....ha ha ha ha ha ha",
            "What do you call an Englishman with an IQ of 50?  Colonel, sir.....ha ha ha ha ha ha",
            "They say an Englishman laughs three times at a joke. The first timewhen everybody gets it, the second a week later when he thinks he getsit, the third time a month later when somebody explains it to him.....ha ha ha ha ha ha",
            "Why do cows wear bells?Because their horns don't work....ha ha ha ha ha ha",
            "my life....ha ha ha ha ha ha",
            "your life....ha ha ha ha ha ha",
            "What did the buffalo say to his son when leaving for college ? bison....ha ha ha ha ha ha",
            " I visited my new friend in his flat. He told me to make myself at home. So I threw him out. I hate having visitors.",
            ]
    randomjoke = random.choice(myjokes)
    print(randomjoke)
    speak(randomjoke)

def motivation():
    moti = ["its a shame for a man to grow old without seeing the beauty and strength his body is capable of",
            "one whos ideal is mortal will die when his ideal dies,but when ones ideal is immortal he himself must become immortal to attain it",
            "pain is only in the mind",
            "Success is not how high you have climbed, but how you make a positive difference to the world.",
            "Never lose hope. Storms make people stronger and never last forever.",
            "strong men make great times,great times make weak men,weak men make tough times,tough times make strong men",
            "All our dreams can come true, if we have the courage to pursue them.",
            "The best time to plant a tree was 20 years ago. The second best time is now.",
            "If people are doubting how far you can go, go so far that you can’t hear them anymore.",
            "Everything you can imagine is real."]
    randommoti = random.choice(moti)
    print(randommoti)
    speak(randommoti)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hr = int(dt.datetime.now().hour)
    if(hr>=0 and hr<12):
        speak("Kaalai Vanakkam !!")
    elif(hr>=12 and hr<18):
        speak("Vannakam !!")
    elif(hr>=18 and hr<20):
        speak("Maaalai Vannakam !!")
    speak("I am Nelson, how can i help?")

def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening")
        print("Listening....")
        audio = rec.listen(source,phrase_time_limit=15)
    try:
        print("Recognizing...")
        query = rec.recognize_google(audio,language='en-in')
        query = query.lower()
        print("You said:", query ,"\n")
    except Exception as e:
        speak("say that again please")
        print("Say that again please")
        return "None"
    return query

    #functions are defined 
def about():
    speak("I am Nelson....I was devloped by students of Artificial intelligence and data science department....I am still learning and open to criticism ")

def func():
    speak("i can ")
    speak("open applications , open websites , search things in google, play youtube videos , tell time and day , tell weather, tell jokes ,fun facts , motivational quotes")
    speak("what do you want to do ?")

def increse_vol():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Get current volume 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(currentVolumeDb  +6.0, None)
    # NOTE: -6.0 dB = half volume !

def decrese_vol():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Get current volume 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(currentVolumeDb  -6.0, None)
    # NOTE: -6.0 dB = half volume !

  
#launch system apps
def app(query):
    appname = query[7:]
    print(appname)
    speak('opening '+ appname)
    appname = appname.replace(" ","")
    os.system(appname)

#open websites
def website(query):
    site = query[5:]
    speak("opening website "+ site)
    site = site.replace(" ","")
    webbrowser.open("www."+site+".com")

#watch youtube videos
def youtube(query):
    utube = query[6:]
    speak("Opening youtube "+ video)
    pywhatkit.playonyt(video)

def google_scearch(ques):
    query = ques
    for j in search(query,tld="co.in",num=10,stop=10,pause=2):
        return(j)


def weather():
    city = "chennai"
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    string = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = string.split('\n')
    time = data[0]
    sky = data[1]
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    pos = strd.find('Wind')
    other_data = strd[pos:]
    print("Temperature is", temp)
    print("Time: ", time)
    print('Sky Description:', sky)
    speak("Temperature is "+ temp)
    speak("The sky is"+ sky)

#main
if __name__ == "__main__":
    greet()
    while True:
        query=listen().lower()

        if "time" in query:
            now = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(now)
            speak(now)

        elif "joke" in query:
            joke()

        elif "motivation" in query:
            motivation()
        
        elif "you" in query:
            about()

        elif "increase volume"  in query:
            increse_vol()
        
        elif "decrease volume" in query:
            decrese_vol()
 
        elif "what can you do" in query:
            func()

        elif "weather" in query:
            weather()
        
        #launch keyword to launch system apps
        elif "launch" in query:
            app(query)

        elif "open easwari" in query:
            webbrowser.open("https://ai.srmeaswari.ac.in/")    

        elif "open uv" in query:
            webbrowser.open("https://theuvofearth.wixsite.com/stage1")

        #open keyword to open websites
        elif "open" in query:
            website(query)

        #watch keyword to search and watch youtube videos
        elif "watch" in query:
            youtube(query)

        elif "search" in query: #returns the best website for asked query
            try:
                result = query[6:]
                speak("giving best results for"+ result)
                google_scearch(result)
                webbrowser.open(google_scearch(result))
            except:
                print("please say something after search")
                speak("please say something after search")

        elif query=="stop" or "end":
            break