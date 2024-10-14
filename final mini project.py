#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import os
import webbrowser
import pywhatkit
import pyjokes
import sys

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice input and return text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-IN')
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that. Could you please repeat?")
            return None
        except sr.RequestError:
            speak("Could not request results, please check your internet connection.")
            return None
        except sr.WaitTimeoutError:
            speak("You took too long to respond, please try again.")
            return None

# Function to open applications
def open_application(query):
    if 'notepad' in query:
        os.system('notepad.exe')
    elif 'command prompt' in query or 'cmd' in query:
        os.system('start cmd')
    elif 'calculator' in query:
        os.system('calc.exe')
    else:
        speak("I can't find that application.")

# Function to handle shutdown and restart
def system_control(query):
    if 'shutdown' in query:
        speak("Shutting down the system.")
        os.system('shutdown /s /t 1')
    elif 'restart' in query:
        speak("Restarting the system.")
        os.system('shutdown /r /t 1')
    else:
        speak("I can't perform that system control operation.")

# Main function for handling user commands
def handle_query(query):
    if query:
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(query, sentences=2)
                speak(f"According to Wikipedia, {result}")
            except Exception:
                speak("Sorry, I couldn't find any information on that topic.")

        elif 'play music' in query:
            query = query.replace("play music", "").strip()
            pywhatkit.playonyt(query)
            speak(f"Playing {query} on YouTube.")

        elif 'what\'s the time' in query:
            time = datetime.datetime.now().strftime("%H:%M %p")
            speak(f"The time is {time}")

        elif 'open youtube and search' in query:
            search_query = query.replace("open youtube and search", "").strip()
            webbrowser.open("https://www.youtube.com")
            speak(f"Searching for {search_query} on YouTube.")
            pywhatkit.playonyt(search_query)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("Opening YouTube")
            
        elif 'open google' in query and 'search' in query:
            query = query.replace("open google and search", "").strip()
            speak(f"Searching for {query} on Google.")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
            speak("Opening Google")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("Opening WhatsApp Web")

        elif 'tell a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'open' in query:
            open_application(query)

        elif 'shutdown' in query or 'restart' in query:
            system_control(query)

        elif 'quit' in query or 'exit' in query:
            speak("Goodbye!")
            sys.exit()
        
        else:
            speak("I couldn't understand that. Please try again.")

# Main loop for voice commands
if __name__ == "__main__":
    speak("Hello! I am your AI assistant. How can I assist you today?")
    try:
        while True:
            query = listen()
            if query:
                handle_query(query)
    except KeyboardInterrupt:
        speak("Goodbye! Have a great day!")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("An error occurred. Please try again later.")
    finally:
        sys.exit()


# In[ ]:




