import pyttsx3
import speech_recognition as sr 
import datetime
import os 
import cv2
import random 
from requests import get
import wikipedia
import webbrowser
import smtplib
import pywhatkit as kit
import pyjokes
import pyautogui
import requests
import time
import sys

engine=pyttsx3.init( 'sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio= r.listen(source, timeout=15,phrase_time_limit=25)

    try:
        print("recognizing..." )
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}")
    except Exception as e:
        speak("say that again please...")
        return "none"    
    return query

def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>0 and hour<=12:
        speak("good morning sir")
    elif hour>12 and hour<18:
        speak("good afternoon sir")  
    else:
        speak("good evening sir ") 
    speak(" please tell me how can i help you")    

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("bhatnagarprakhar09@gmailcom", "PrakhaR@23")
    server.sendmail("bhatnagarprakhar09@gmail.com", to, content)

def news():
    main_url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f30982fc41924c25968abba02c5842ed"

    main_page= requests.get(main_url).json()
    articles=main_page["articles"]
    head=[]
    day=["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")
    



if __name__=="__main__":
    takecommand()
    speak("this is gideon. welcome Prakhar Bhatnagar")  
    wish()
    while True:
    

        query= takecommand().lower()
        #logic building
        
        if "open excel" in query:
            npath="C:\\Users\\bhatp\\Downloads\\Power BI Dataset.xlsx"
            os.startfile(npath)
        elif "close excel" in query:
            speak("okay sir, closing excel")
            os.system("taskkill /f /im Power BI Dataset.exe")


        elif "set alarm" in query:
           nn=int(datetime.datetime.now().hour)
           if nn==22:
                music_dir="D:\\music"
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
    
        elif "tell a joke" in query:
            joke=pyjokes.get_joke()
            speak(joke)

    
        elif "open cmd" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(58)
                if k==27:
                    break;   
            cap.release()
            cv2.destroyAllWindows()

        
        
        elif "play music" in query:
            music_dir="D:\\music"
            songs= os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif "close music" in query:
            speak("okay sir, closing music")
            os.system("taskkill /f /im D:\\musicśś ")


        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        #elif "open NIT jalandhar website" in query:
           # webbrowser.open("www.nitj.com")
        
        elif "open google" in query:
            speak ("sir what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+917310521969", "this is testing protocol",0,0)

        
        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()  

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")



        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        elif "sleep the system" in query:
            os.system("rund1132.exe powrprof.dll, SetSuspendState 0,1,0")


        elif "play songs on youtube" in query:
            kit.playonyt("see you again")
        
        elif "send email to reena" in query:
                speak("what should i say?")
                query= takecommand().lower()
                if "send a file" in query:
                    email = "bhatnagarprakhar09@gmail.com"
                    password="PrakhaR@23"
                    send_to_email="bhatreena27@gmail.com"
                    speak("okay sir, what is the message for this email")
                    query= takecommand().lower()
                    message=query2
                    speak("sir, please enter the correct path of the file")
                    file_location= input("please enter the path here")

                    speak("please wait, i am sending email now")

                    msg=MIMEMultipart()
                    msg["from"]= email
                    msg["to"]= send_to_email
                    msg["subject"]=subject

                    msg.attach(MIMEText(message, "plain"))

                    #setup the attachment
                    filename= os.path.basename(file_location)
                    attachment= open(file_location, "rb")
                    part= MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", "attachment; filename= %s" % filename)
                    
                    #attach the attachment to the MIMEMultipart object
                    msg.attach(part)
                    
                    server=smtplib.SMTP('smtp.gmail.com',587)
                    server=starttls()
                    server.login(email, password)
                    text=msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to reena")

                else:
                    email= "bhatnagarprakhar09@gmail.com"
                    password= "PrakhaR@23"
                    send_to_email= "bhatreena27@gmail.com"
                    message= query

                    server= smtplib.SMTP("smtp.gmail.com")
                    server.starttls()  
                    server.login(email,password) 
                    server.sendmail(email,send_to_mail, message) 
                    server.quit()
                    speak("email has been sent to reena")

               

        elif "no gideon you can rest" in query:
            speak("thank you sir, have a nice day")
            sys.exit()
        
        
        speak("sir, do you have any other work? ")

