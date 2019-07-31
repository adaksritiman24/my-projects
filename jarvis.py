import pyttsx3
import random
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
	engine.say(audio)
	engine.runAndWait()
def wishme():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning")
	elif hour>=12 and hour<18:
		speak("Good afternoon")
	else:
		speak("Good Evening")		
	speak("I am Jarvis")	

def takeCommand():
	#takes microphone input
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listning.....")
		r.pause_threshold=1
		audio=r.listen(source)

	try:
		print("Recognizing...")
		query=r.recognize_google(audio,language="en-in")
		print(f"User said: {query}\n")
	
	except Exception as e:
		#print(e)
		print("Check your internet connection/Say something ")
		return "None"	
	
	return query	


wishme()
while True:
	q=takeCommand().lower()

	if "what is a " in q:
		q=q.replace("what is a ","")
		result=wikipedia.summary(q,sentences=2)
		speak(result)
	if ("what is " in q):
		q=q.replace("what is ","")
		result=wikipedia.summary(q,sentences=2)
		speak(result)		
	if ("who is " in q):
		q=q.replace("who is ","")
		result=wikipedia.summary(q,sentences=2)
		speak(result)
	if "wikipedia" in q:
		speak("ok")
		speak("Searching Wikipedia...")
		q=q.replace("wikipedia","")
		results=wikipedia.summary(q,sentences=2)
		speak("According to wikipedia")
		speak(results)
	elif "open youtube" in q:
		speak("ok")
		speak("Opening youtube")
		webbrowser.open("youtube.com")
	elif("play a song" in q) or ("play song" in q):
		speak("playing a song")
		song_path="C:\\Users\\Sritiman Adak\\Desktop\\songs"
		song=os.listdir(song_path)
		os.startfile(os.path.join(song_path,song[random.randint(0,len(song)-1)]))
	elif("play a music" in q) or ("play music" in q):
		speak("playing a music")
		song_path="C:\\Users\\Sritiman Adak\\Desktop\\songs"
		song=os.listdir(song_path)
		os.startfile(os.path.join(song_path,song[random.randint(0,len(song)-1)]))				
	elif "open google" in q:
		speak("ok")
		speak("opening google")		
		webbrowser.open("google.com")
	elif "open stack overflow" in q:
		speak("ok")
		speak("opening stackoverflow")		
		webbrowser.open("stackoverflow.com")
	elif "the time" in q:
		strtime=datetime.datetime.now().strftime("%H:%M:%S")	
		speak("the current time is,")
		speak(strtime)
	elif "open iron man fan club" in q:
		speak("opening iron man fan club")
		path="C:\\Users\\Sritiman Adak\\Desktop\\py_examples\\iron_man_fan_club.py"
		os.startfile(path)
	elif "goodbye" in q:
		speak("Ok")
		speak("Goodbye")
		break		
	elif "good bye" in q:
		speak("Ok")
		speak("Goodbye")
		break					
