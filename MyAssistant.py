import openai
from apikey import api_data
import pyttsx3
import webbrowser 
import speech_recognition as sr
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from MY_AI import Ui_MainWindow
import pywhatkit
from pywikihow import WikiHow , search_wikihow
import wikipedia
import webbrowser as web
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

#ans= Reply("what do you mean by machine learning? Explain.")
#print(ans)

engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#speak("Hey!! How are you?")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
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



    def TaskExecution(self):
        speak('Hey, How are you?')
        while True:
            self.query = self.takeCommand().lower()
            ans = Reply(self.query)
            print(ans)
            speak(ans)
            if 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
            if 'open google' in self.query:
                webbrowser.open("www.google.com")
            if 'open whatsapp' in self.query:
                webbrowser.open("www.whatsapp.com")
            if 'bye' in self.query:
                break
############################################################

def GoogleSearch(term):
    query = term.replace("Erica","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("Explain","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")
    writeab = str(query)

    Query = str(term)
    pywhatkit.search(Query)
    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query, max_results= max_result)
        assert len(how_to_func) == 1   #put in a sequence
        how_to_func[0].print()
        speak(how_to_func[0].summary)

    else:
        search = wikipedia.summary(Query,2)  #search your query
        speak(f": According to your Search : {search}")



#############################################################
    
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("GUI//Graphics.gif")
        self.ui.Erica.setMovie(self.ui.movie)
        self.ui.movie.start()


        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.label.setText(label_date)
        self.ui.label_2.setText(label_time)


app = QApplication(sys.argv)
erica = Main()
erica.show()
sys.exit(app.exec_())
    