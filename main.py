import os
import openai
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib
from news import speak_news, getNewsUrl
from OCR import OCR
from diction import translate
from helpers import *
from youtube import youtube
from sys import platform
import os
import getpass
from gtts import gTTS
from playsound import playsound
from pygame.mixer import Sound
import pygame
from pydub import AudioSegment
from pydub.playback import play
import pyrubberband as pyrb
import soundfile as sf
import time

openai.organization = "org-bMnHOkBSJP5f6k5JD1oqQulu"
openai.api_key = "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"
openai.Model.list()


for x in range(100):
    import os
    if os.path.exists(f"faster{x}.mp3"):
        os.remove(f"faster{x}.mp3")
        os.remove(f"response{x}.mp3")
    else:
        continue

os.environ["PATH"] += os.pathsep + "C:/Python310/ffmpeg/bin"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
pygame.mixer.init(44100, -16,2,2048)
pygame.mixer.init() 
pygame.init()

listPertanyaan = []
listJawaban = []
x = 0
while True:
    # question = "bagaimana kabarmu"
    playsound(f"active.mp3")
    question = takeCommand().lower()
    prompt = f"Berikut percakapan dengan asisten AI. Asistennya sangat membantu, kreatif, pintar, dan sangat ramah.\n\nManusia: Halo, siapa kamu?\nAI: Saya adalah AI yang dibuat oleh OpenAI. apa yang bisa saya bantu hari ini?\Manusia:"
    for y in range(len(listPertanyaan)):
        prompt = prompt + f" " + listPertanyaan[y] + "\nAI: " + listJawaban[y] + "\nManusia:"
    prompt = prompt + f" {question}\nAI:"

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
    )
    
    listPertanyaan.append(question)
    listJawaban.append(response["choices"][0]["text"])

    # speak(response["choices"][0]["text"])
    gTTS(text=response["choices"][0]["text"], lang='id', slow=False).save(f"response{x}.mp3")


    # sound = Sound(f"response{x}.wav")
    # sound.play()

    import subprocess
    import librosa

    # Mempercepat audio menjadi 2 kali lipat
    subprocess.run(["ffmpeg", "-i", f"response{x}.mp3", "-filter:a", "atempo=1.5", "-vn", f"faster{x}.mp3"])

    duration = librosa.get_duration(filename=f"faster{x}.mp3")    

    playsound(f"faster{x}.mp3")

    print("")
    print("A:"+ response["choices"][0]["text"])
    
    if duration>5:
        time.sleep(int(duration)-3)
    x += 1

