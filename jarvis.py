import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import Music_library
import google.generativeai as genai
import requests as req

recognizer = sr.Recognizer()
engine = pyttsx3.init()

gemini_api = "Gemini-api-key"
news_api = 'Api-key'

def speak(text):
    engine.say(text)
    engine.runAndWait()

def AIprocess(command):
    genai.configure(api_key=gemini_api)

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(command)
    return (response.text)

def process_command(c):
    if "open chrome" in c.lower():
        wb.open("https://chrome.com")

    elif "open youtube" in c.lower():
        wb.open("https://youtube.com")

    elif "open linkedin" in c.lower():
        wb.open("https://linkedin.com")

    elif "open whatsapp" in c.lower():
        wb.open("https://whatsapp.com")

    elif "open chatGPT" in c.lower():
        wb.open("https://chatgpt.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = Music_library.music[song]
        wb.open(link)
    
    elif 'news' in c.lower():
        r = req.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}')
        if r.status_code==200:
            data = r.json()
            articles = data.get(articles,[])
            for article in articles:
                speak(article['title'])

    else:
        output = AIprocess(c)
        print(output)
        speak(output)

if __name__=='__main__':
    speak("Initializing Alexa...")

    while True:
        #Listen for waks word "Alexa" only"
        #Obtain audio from mic
        r = sr.Recognizer()

        print("recognizing...")
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower()=="alexa"):
                speak("Yes")                                         #Listening the command

                with sr.Microphone() as source:
                    print("Alexa is active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    process_command(command )

        except Exception as e: 

            print("Error ;{0}".format(e))