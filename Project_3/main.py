import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio
import musicLibary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

reognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "***************************************"


def speak(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3')

#     # Initialize Pygame mixer
#     pygame.mixer.init()

#     # Load the MP3 file
#     pygame.mixer.music.load('temp.mp3')

#     # Play the MP3 file
#     pygame.mixer.music.play()

#     # Keep the program running until the music is playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)


#     os.remove("temp.mp3")



def aiProcess(command):
    client = OpenAI(api_key="sk-proj-wZc8qvY8W7YAgzfpbTIET3BlbkFJh0P1WfhFfxOTqjmsBUra")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant  named jarvis skilled in general task like Alexa and Goodle cloud.Give short repsponse please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content


def  processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        # Checking if the request was successful
        if r.status_code == 200:
            # Parsing the JSON r
            data = r.json()
            # Extracting headlines
            articles = data.get('articles',[])
            # Printing the headlines
            for article in articles:
                speak(article['title'])
    else:
        # let OpenAI Handles the request
        output = aiProcess(c)
        speak(output)


    


if __name__ == "__main__":
    
    speak("Initializing Jarvis...")
    
    while True:
        # Listen for the wake word "jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recongnizing..")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("ya")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
             
        except Exception as e:
            print("Error; {0}".format(e))