from cProfile import run
import speech_recognition as spr
import pyttsx3
import pywhatkit

listener=spr.Recognizer()
google=pyttsx3.init()
voices=google.getProperty("voices")
google.setProperty("voice",voices[1].id)

def googletalk(text):
    google.say(text)
    google.runAndWait()    

def usercommand():
    try:
        with spr.Microphone() as source:
            print("Speak now... ")
            voice =listener.listen(source)
            command= listener.recognize_google(voice)
            command=command.lower()
            
            if "google" in command:
                command=command.replace("google","")
                print(command)
    except:
        pass
    return command

def rungoogle():
    command=usercommand()
    if "play" in command:
        song=command.replace("play","")
        print(song)
        googletalk("playing"+song)
        pywhatkit.playonyt(song)
    else:
        
        googletalk('I could not hear you.')
        googletalk('Try again')

rungoogle()
