import pyttsx3
    #download by using:- pip install pyttsx3
import datetime
    #inbuilt library


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
'''print(voices[1].id)'''
engine.setProperty('voice',voices[0].id)
#you can convert 0 to 1 or more to change voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=3 and hour<12:
             speak("Good Morning sir")
        
        elif hour>=12 and hour<17:
            speak("Good Afternoon sir")

        elif hour>=17 and hour<20:
            speak("Good Evening sir") 
        else :
            speak("Good night sir") 
    #you can change sir to ma'am if you are female
if __name__ == "__main__":
    wishMe()