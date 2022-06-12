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
import time
import schedule
import speedtest
import pyautogui

r = sr.Recognizer()
mymic = sr.Microphone(device_index=1)

engine = pyt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 190)
engine.setProperty('volume', 0.7)

def joke():
    myjokes = ["bored of being bored because being bored is boring....ha ha ha ha ha ha",
            "What do you call an Englishman with an IQ of 50?  Colonel, sir.....ha ha ha ha ha ha",
            "They say an Englishman laughs three times at a joke. The first timewhen everybody gets it, the second a week later when he thinks he getsit, the third time a month later when somebody explains it to him.....ha ha ha ha ha ha",
            "Why do cows wear bells?Because their horns don't work....ha ha ha ha ha ha",
            "my life....ha ha ha ha ha ha",
            "your life....ha ha ha ha ha ha",
            "What did the buffalo say to his son when leaving for college ? bison....ha ha ha ha ha ha",
            " I visited my new friend in his flat. He told me to make myself at home. So I threw him out. I hate having visitors....ha ha ha ha ha ha",
            ]
    randomjoke = random.choice(myjokes)
    print(randomjoke)
    speak(randomjoke)

def motivation():
    moti = ["its a shame for a man to grow old without seeing the beauty and strength his body is capable of",
            "one whos ideal is mortal will die when his ideal dies , but when ones ideal is immortal he himself must become immortal to attain it",
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

def list():
    print("How are you - General interaction\nTell about yourself - About our virtual assistant\nwho are you - About our virtual assistant\nWhat can you do - Tell about the things VA can do \nWho made you / Who created you - About the creators\nTime - Will tell current date and time\nweather - Will tell weather of current location\njoke - Tell a joke\nmotivation - Tell a motivational quote\nopen <name> - Open the given website name\nsearch <name> - Search the given name in google\nIncrease volume - Will increase volume by 28% \nDecrease volume - Will decrease volume by 28%\nlaunch <app_name> - Launch apps in system \nopen uv - Element of surprise  \nSleep - Nelson will go to sleep\nRoast - Roast")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hr = int(dt.datetime.now().hour)
    if(hr>=0 and hr<12):
        speak("Good morning !!")
    elif(hr>=12 and hr<18):
        speak("Good afternoon !!")
    elif(hr>=18 and hr<20):
        speak("Good evening  !!")
    speak("I am Nelson, how can i help?")

def speed():
    st = speedtest.Speedtest()
    d_speed = st.download()
    u_speed = st.upload()
    KB = 1024
    MB = KB * 1024
    d_mb = int(d_speed/MB)
    u_mb = int(u_speed/MB)
    print(f"Download speed : {d_mb} MBPS")
    speak(f"Your download speed is {d_mb} MB per second")
    print(f"Upload speed : {u_mb} MBPS")
    speak(f"Your upload speed is {u_mb} MB per second")

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
        speak(" Say that again human")
        print("Say that again human")
        return "None"
    return query

    #functions are defined 
def about():
    speak("I am Nelson....I was devloped by students of Artificial intelligence and data science department....I am still learning and open to criticism ")

def func():
    speak("i can ")
    speak("open applications , open websites , search things in google, play youtube videos , tell time and day , tell weather, tell jokes ,fun facts , motivational quotes , control system volume")
    speak("what do you want to do ?")

def hydrate():
    print("Drink water human...stay hydrated ")
    speak("Drink water human...stay hydrated ")

def takebk():
    print("take a break human...you deserve it")
    speak("take a break human...you deserve it")

def remind():
    speak("what you want me to remind ?")
    thing = listen()
    print(thing)

def increse_vol():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # Get current volume 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if currentVolumeDb > -5.409796714782715:
        print("volume is more than 70 percent...please keep it below 70")
        speak("volume is more than 70 percent...please keep it below 70")
    else:
        volume.SetMasterVolumeLevel(currentVolumeDb  +6.0, None)
    # NOTE: -6.0 dB = half volume !

def set_vol(x):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # Get current volume 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    print(volume.GetMasterVolumeLevel())
    print(volume.GetVolumeRange())
    #volume.SetMasterVolumeLevel(currentVolumeDb  +6.0, None)
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
    #appdict = {"paint":,"excel":,"spreadsheet":,"word":,"powerpoint":,"presentation":,"google":,"chrome":}
    appname = query[7:]
    print(appname)
    speak('opening '+ appname)
    appname = appname.replace(" ","")
    os.system("excel")
    return

#open websites
def website(query):
    site = query[5:]
    speak("opening website "+ site)
    site = site.replace(" ","")
    webbrowser.open("www."+site+".com")

def news(query):
    headlines = query[12:]
    speak("opening todays news"+ headlines)
    headlines = headlines.replace(" ","+")
    webbrowser.open("https://news.google.com/search?for="+headlines+"&hl=en-IN&gl=IN&ceid=IN%3Aen")

#watch youtube videos
def youtube(query):
    utube = query[6:]
    speak("Opening youtube "+ utube)
    pywhatkit.playonyt(utube)

def google_scearch(ques):
    query = ques
    for j in search(query,tld="co.in",num=10,stop=10,pause=2):
        return(j)

def gogo():
    slepcom = ["Mention the duration you want me to go sleep",
    "Mention the duration you dont want me to disturb you",
    "Mention the duration you want me to be silent",
    "Mention the duration you want inner peace"]
    comm = random.choice(slepcom)
    print(comm)
    speak(comm)
    ss = listen()
    ss_int = int(ss)
    #ss = int(input())  #input is given manually we can convert it to be directly given by voice
    time.sleep(ss_int)
    print("Nelson is back")
    speak("nelson is back...yyyyyaaaaaay")
    
def roast():
    rlist = ["Light travels faster than sound, which is why you seemed bright until you spoke.",
             "You have so many gaps in your teeth it looks like your tongue is in jail.",
             "time illa",
             "Your face makes onions cry.",
             " You bring everyone so much joy… when you leave the room."]
    rand = random.choice(rlist)
    print(rand)
    speak(rand)

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

def devlopers():
    speak("they are group of Artificial intelligence and data science students from easwari engineering college....let me open their linked in profiles for you")
    webbrowser.open("https://www.linkedin.com/in/naveen-kumar-s-921990210")
    webbrowser.open("www.linkedin.com/in/arjun-prakash-589348211")
    webbrowser.open("https://www.linkedin.com/in/raghuram-s-647b18213")
    webbrowser.open("https://www.linkedin.com/in/hari-vigneshwaran-97499a213")

def wiki(query):
    speak("searching .......")
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=2)
    speak("Accroding to wikipedia")
    speak(result)

str = " NELSON - Voice Assistant "
#main
if __name__ == "__main__":
    print("")
    print("#"*50)
    print(str.center(50,"*"))
    print("#"*50)
    print("")
    greet()
    schedule.every(2).minutes.do(hydrate)
    schedule.every(1).minutes.do(takebk)
    while True:
        schedule.run_pending()
        query=listen().lower()

        if "time" in query:
            now = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(now)
            speak(now)

        elif "joke" in query:
            joke()

        elif "motivation" in query:
            motivation()
        
        elif "wikipedia" in query:
            wiki(query)
        
        elif ("headlines" in query) or ("news" in query):
            news(query)

        elif 'minimise the windows 'in query or'minimise the window'in query :
            speak("minimize the window")
            pyautogui.hotkey('Win','d')

        elif 'maximize the windows'in query or'maximize the window'in query :

            speak("maximizing the window")
            pyautogui.hotkey('Win', 'd')

        elif 'new tab'in query:
            pyautogui.hotkey('ctrl','t')

        elif 'new file'in query:
            pyautogui.hotkey('ctrl','n')

        elif 'switch windows'in query  or 'switch tab'in query:
            pyautogui.hotkey('ctrl','shift','tab')

        elif 'switch the app' in query:
            pyautogui.hotkey('alt','tab')

        elif 'close window' in query:
            pyautogui.hotkey('alt','f4')

        elif "tell about you" in query:
            about()

        elif "who are you" in query:
            about()

        elif "increase volume"  in query:
            increse_vol()
        
        elif "decrease volume" in query:
            decrese_vol()
 
        elif "what can you do" in query:
            func()

        elif "weather" in query:
            weather()

        elif "set" in query:
            y = query[10:]
            y  = float(y)
            k = y/100
            set_vol(k)
        
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

        elif "how are you" in query:
            speak("i am fine human...how about you ?")
        
        elif query=="show commands":
            list()

        elif query=="sleep":
            gogo()

        elif (query == "who created you") or (query == "who made you"):
            devlopers()
        
        elif "roast" in query:
            roast()
        
        elif "remind" in query:
            remind()

        elif "speed" in query:
            print("working on it")
            speak("working on it")
            speed()

        #Alarm
        elif "going to sleep" in query or "wake me" in query:
            speak("When should I wake you up sir ? Enter the time")
            time = input("Enter the Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to Wake up Sir")
                    playsound("surprise.mp3")
                    speak("Alarm Closed")

                elif now>time:
                    break

        elif "know hari" in query or "know naveen" in query or "know raghu" in query or "know kesava" in query or "know arjun" in query:
                speak(f"yes i know him. Do you believe in god? i do believe. He is my god. becuase of him im able to talk to you. he is a very nice person. You would like him if you start talking with him")
        
        else:
            continue
        #elif query=="stop" or "end":
            #exit()