import os
import openai
import pyttsx3
import speech_recognition as sr
import os
from OCR import OCR
import os
from gtts import gTTS
from playsound import playsound
from pygame.mixer import Sound
import pygame
import time
import subprocess
import librosa

openai.organization = "org-bMnHOkBSJP5f6k5JD1oqQulu"
openai.api_key = 'YOUR OPENAI API KEY HERE'
openai.Model.list()

def Listening() -> str:
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)
    with mic as source:
        print('Listening...')
        r.pause_threshold = 1.5
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='id')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)

        print('Say that again please...')
        return 'None'
    return query

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
    question = Listening().lower()
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
    # sound.play()2A 

    # Mempercepat audio menjadi 2 kali lipat
    subprocess.run(["ffmpeg", "-i", f"response{x}.mp3", "-filter:a", "atempo=1.5", "-vn", f"faster{x}.mp3"])

    duration = librosa.get_duration(filename=f"faster{x}.mp3")    

    playsound(f"faster{x}.mp3")

    print("")
    print("A:"+ response["choices"][0]["text"])
    
    if duration>5:
        time.sleep(int(duration)-3)
    x += 1

