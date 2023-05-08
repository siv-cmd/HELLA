import pyttsx3
import speech_recognition as sr
import os 
import subprocess
import twilio
import tkinter
import webbrowser
import time
import requests
import datetime
import feedparser
import ctypes
import shutil
import operator
import pywhatkit
import wikipedia
import json
import smtplib
import wolframalpha
from twilio.rest import Client
from clint.textui import progress 
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from win32com.client import wincl
from urllib.request import urlopen
import pyautogui
from INTRO import play_gif
import snowman
import speedtest
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)
engine.setProperty("pitch", 50)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("good morning siva")
    elif hour>= 12 and hour<18:
        speak("good afternoon  siva")
    else:
        speak("good evening siva")

    assname =("welcome back siva what can do for you")
    speak(assname)

def eat():
    hour = int(datetime.datetime.now().hour)
    if hour>= 8 and hour<11:
        speak("have you had your breakfast")
        food = input("(yes/no)")
        if food == "yes":
            speak("it's good to hear that")
        elif food == "no":
            speak("can i order you food")
            webbrowser.open("swiggy.com")
    else:
        speak("")

wake_word = "hella"

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("fetching..")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        print(e)
        print("I am not programmed for that")
        return "None"

    return query

def email(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sivacomrade2003@gmail.com', '')
    server.sendmail('sivacomrade2003@gmail.com', to,content)
    server.close()
    
if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishme()
    
    while True:
        query = command().lower()
        if 'what is ' in query or 'who is ' in query:
            speak('fetching information across the web')
            query = query.replace("what is","")
            query = query.replace("who is ","")
            results = wikipedia.summary(query, sentences = 10)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif "introduce yourself" in query:
            speak("allow me to introduce myself i am hella an emerging virtual artifical intelligence and i am here to assist you")
        elif 'open youtube' in query:
            speak("here you go siva enjoy an entertanment\n")
            webbrowser.open("youtube.com")
        elif 'open whatsapp' in query:
            speak("here is your whatsapp siva\n")
            webbrowser.open("web.whatsapp.com")
        elif 'open stackoverflow' in query:
            speak("opening stack over flow but i recommend chatgpt\n")
            webbrowser.open("stackoverflow.com")
        elif 'spotify' in query or 'play a song ' in query:
            speak("playing music")
            codepath = r"C:\Users\harih\AppData\Roaming\Spotify\Spotify.exe"
            os.startfile(codepath)
            
        elif 'mail to siva' in query:
            try:
                speak("what's the message")
                content = command()
                to = "sivacomrade2003@gmail.com"
                email(to,content)
                speak("mail has been sent successfully")
            except Exception as e:
                print(e)
                speak("someting went wrong check code of me")
                
        elif 'send a mail' in query:
            try:
                speak("what should i say")
                content = command()
                speak("who is the receiver")
                to = input()
                email(to,content)
                speak("mail has sent")
            except Exception as e:
                print(e)
                speak("there some problem in my code so can't do it")
                
        elif 'how are you' in query:
            speak("i am fine, thank you")
            speak("how about you ")
        elif 'fine' in query or 'good' in query:
            speak("it's good to know that your fine")
        elif 'not fine' in query or 'not good' in query or 'not feeling well' in query or 'exhausted' in query or 'bored' in query or 'feelling tried' in query:
            speak("sorry to here that ")
        elif "what's your name" in query or "what is your name" in query:
            speak("i am hella")
        elif 'exit ' in query:
            speak("thanks for giving me you time")
            exit()
        elif "who made you " in query or "who created you" in query:
            speak("i have programmed by siva in just 5 freaking days")
        elif 'joke' in query:
            speak("playing jokes")
            webbrowser.open("https://www.youtube.com/watch?v=k9nRLWuqEYc")
        elif "calculate " in query:
             app_id = "UW98G9-9KTTVV7WUG"
             Client = wolframalpha.Client(app_id)
             indx = query.lower().split().index('calculate')
             query = query.split()[indx + 1:]
             res = Client.query(' '.join(query))
             answer = next(res.results).text
             print("the answer is"+ answer)
             speak("the answer is " + answer)
        elif 'search' in query :
             query = query.replace("serach", "")
             webbrowser.open(query)
        elif "who i am " in query:
            speak("you must siva's class mate")
        elif 'open ppt' in query:
            speak("opening power point presentation")
            power =r
            os.startfile(power)
        elif 'who are you ' in query:
            speak("i am presonal assitant of siva")
        elif 'reason for you ' in query:
            speak("i was mainly created to give ship cordinates")
        elif 'hai hella' in query:
            speak("nice to meet you friend ")
        elif "news" in query:
             try:
                 json0bj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\fdc5d783bd8c41c58fda9fa4c13db42e\\''')  
                 data = json.load(json0bj)
                 i = 1
                 
                 speak("here are some top news from the times of india")
                 print('\'============= TIMES OF INDIA ============\'')

                 
                 for item in data['articles']:
                     
                     print(str(i) + '.' + item['title'] + '\n')
                     print(item['description'] + '\n')
                     speak(str(i) + '.' + item['title'] + '\n')
                     i += 1
             except Exception as e:
                 
                 print(str(e))
                 
        elif 'lock screen' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'empty recycle bin ' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound =True)
            speak("recycle bin recycled")
            
        elif "kill code"  in query:
            speak("kill code confirmed")
            a = int(command())
            time.sleep(a)
            print(a)
        elif "where is " in query:
            query = query.replace("where is "," ")
            location = query
            speak("locating")
            speak(location)
            webbrowser.open("https://www.google.nl / maps /place" + location + "")
        elif "say hai to" in query:
            query = query.replace("say hai to ","")
            hai = query
            speak("hai nice to meet you")
            speak(hai)
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "hella camera" ,"img.jpg")
            speak("your photos are saved in your computer")
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "hibernate" in query:
            speak("hibernating")
            subprocess.call("shutdown /h")
        elif "sign out" in query:
            speak("make sure to close the running application")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        elif "locate " in query:
            query = query.replace("locate","")
            port = query
            speak("locating")
            speak(port)
            webbrowser.open("https://www.shipxplorer.com / port/" + port + "")
        elif "weather" in query:
            api_key =  "a7ef2bdf0609ea353ec504b536e4d47c"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = command()
            complete_url = base_url  + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
            
            if x["code"] !="404":
                y =x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy =y["humidity"]
                z = x["weather"]
                weather_description =z[0]["description"]
                print(" temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))

            else :
                speak("weather server is down")  
        elif "send message " in query:
            account_sid = 'AC66fc871b87a95d3f19f94bef1fd2d8ea'
            auth_token = '2950a3413650df6378cfd658fa67fc99'
            client = Client(account_sid, auth_token)
            message = client.message \
                            .create(
                                body = command(),
                                form ='sender no',
                                to = 'receiver no'
                    )
            print(message.sid)

        elif "good morning" in query:
             speak("a warm" + query)
             speak("how are you siva")
        elif 'good aftenoon' in query:
             speak("a pleasent"+ query)
        elif 'good evening' in query:
            speak("how was the day")
        elif 'good night ' in query:
            speak("have great sleep")
        elif "how are you " in query:
             speak("i'm fine ")
        elif "solve" in query:
             client = wolframalpha.Client("UW98G9-9KTTVV7WUG")
             res = client.query(query)
             try:
                print (next(res.results).text)
                speak (next(res.results).text)
             except StopIteration:
                print ("No results")
        elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

        elif "pause" in query:
              pyautogui.press("k")
              speak("video paused")
        elif "play" in query:
              pyautogui.press("k")
              speak("video played")
        elif "mute" in query:
              pyautogui.press("m")
              speak("video muted")

        elif "volume up" in query:
             from keyboard import volumeup
             speak("Turning volume up")
             volumeup()
        elif "volume down" in query:
            from keyboard import volumedown
            speak("Turning volume down")
            volumedown()
        elif "shutdown the system" in query:
                speak("Are You sure you want to shutdown")
                shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                if shutdown == "yes":
                    os.system("shutdown /s /t 1")
                
                elif shutdown == "no":
                     break  
        elif "translate" in query:
                        from Translator import translategl
                        query = query.replace("hella","")
                        query = query.replace("translate","")
                        translategl(query)              
        elif "open" in query:   
                    query = query.replace("open","")
                    query = query.replace("hella","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 
        elif "i love you" in query:
            speak("i am not programmed for that")
        elif "hai " in query:
            speak("hello i am hella how can i help you")
        elif 'play' in query:
            song = query.replace('play',"")
            speak("playing" + song)
            pywhatkit.playonyt(song)
        elif "download" in query:
            words = query.split()
            url = words[words.index("download") + 1]
            response = requests.get(url)
            if response.status_code == 200:
                speak("Download successful!")
            else:
                speak("Download failed.")
        elif "what's your birthday" in query:
            speak("march 18 2023")
        elif "zoom in" in query:
            pyautogui.hotkey('ctrl', '+')
            speak("Zooming in...")
        elif "zoom out" in query:
            pyautogui.hotkey('ctrl','-')
            speak("zooming out")
        elif "move left" in query:
             pyautogui.press('left')
             speak("Moving left...")
        elif "move right" in  query:
             pyautogui.press('right')
             speak("Moving right...")
        elif "next slide" in query:
            pyautogui.press('right')
            print("Showing next slide...")
        elif "prevoius slide " in query:
            pyautogui.press('left')
            print("prevoius slide")
        elif "judges" in query:
            speak("hello judges it's a pleasure to meet you")
        elif "what is the meaning of your name" in query:
            speak("i don't know it siva didn't tell me that")
        if "navigate " in query:
            query = query.replace("navigate","")
            vessel = query
            speak("tracking")
            speak(vessel)
            url = f"https://services.marinetraffic.com/api/exportvessel/v:}/timespan=24/protocol=jsono/shipname:{vessel}"
            response = requests.get(url)
            json_data = response.json()
            url = json_data["url"]
            webbrowser.open(url)
