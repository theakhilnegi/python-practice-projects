import requests
import json
from win32com.client import Dispatch

def sound(txt):
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(txt)
flag=1
# By changing technology to other keywords like business entertainment etc...  you can get different news...
url = ("http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=df3a7e5f0d2e43d2bcebf863f76274a2")
response = requests.get(url)
sound("good morning boss akhil negi. today's news headlines are")
for i in range(len(response.json()["articles"])):
    if response.json()["articles"][i]["description"] != None:
        sound(flag)
        sound(response.json()["articles"][i]["description"])
        flag+=1

