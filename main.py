import openai
from apikey import api_data
import pyttsx3
import webbrowser
import speech_recognition as sr
import pyperclip
import os

openai.api_key=api_data

'''Bob: How are you?
Openai: I am fine'''

completion = openai.Completion()
def Reply(question):
    prompt= f"Vini: {question}\n Erica: "
    response= completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Vini'], max_tokens= 1000)
    answer= response.choices[0].text.strip()
    return answer

ans= Reply("what do you mean by machine learning? Explain.")
print(ans)

engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hey!! How are you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threashold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query= r.recognize_google(audio, language='en-in')
        print("Vini said: {} \n".format(query))
    except Exception as e:
        print("say that again..")
        return "None"
    return query





if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        ans = Reply(query)
        print(ans)
        speak(ans)
        if 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        if 'open google' in query:
            webbrowser.open("www.google.com")
        if 'open whatsapp' in query:
            webbrowser.open("www.whatsapp.com")
        if 'bye' in query:
            break

