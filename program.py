import os
import pyttsx3
import time

        
Text = input("Enter the text: ")

print("please wait...processing")

engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(Text)


time.sleep(3)

engine.setProperty('voice', voices[0].id)
engine.say(Text)

engine.runAndWait()