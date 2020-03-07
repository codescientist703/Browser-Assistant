from facebook import facebook
from common import common
from google import google
import pyttsx3 
from youtube import youtube
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import speech_recognition as sr
import time
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
class main:
    def recognize_speech_from_mic(self,recognizer, microphone):
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")
        if not isinstance(microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")
        with microphone as source:
            recognizer.pause_threshold = 1
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }
        try:
            print('Recognizing the speech')
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            response["error"] = "Unable to recognize speech"
        return response

recognizer = sr.Recognizer()
microphone = sr.Microphone()
options = webdriver.ChromeOptions()
#options.add_experimental_option("excludeSwitches", ['enable-automation']);
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/chromedriver.exe",options=options)
driver.maximize_window()
PROMPT_LIMIT = 5
speak("Hello my name is Ulla Brita. How may I help you ?")
while(1):
    for i in range(PROMPT_LIMIT):
        speak("I am listening")
        print("I am listening")
        #engine.say("I am listening") 
       # engine.runAndWait() 
        keyword = main().recognize_speech_from_mic(recognizer, microphone)
        if keyword["transcription"]:
            break
        if not keyword["success"]:
            break
        print("I didn't catch that. What did you say?")
    print(keyword["transcription"].lower())
    if "facebook" in keyword["transcription"].lower():
        facebook().start(driver)
    elif "new tab" in keyword["transcription"].lower():
        common().opentab(driver)
    elif "profile" in keyword["transcription"].lower():
        facebook().profile(driver)
    elif "go back" in keyword["transcription"].lower():
        common().back(driver)
    elif "go forward" in keyword["transcription"].lower():
        common().forward(driver)
    elif "logout" in keyword["transcription"].lower():
        facebook().logout(driver)
    elif "message" in keyword["transcription"].lower():
        facebook().message(driver)
    elif "scroll down" in keyword["transcription"].lower():
        common().scrolldown(driver)
    elif "scroll up" in keyword["transcription"].lower():
        common().scrollup(driver)
    elif "play" in keyword["transcription"].lower() or "pause" in keyword["transcription"].lower():
        youtube().playpause(driver)
    elif "open notifications" in keyword["transcription"].lower() or "close notifications" in keyword["transcription"].lower():
        facebook().notification(driver)
    elif "open google" in keyword["transcription"].lower():
        print("What do want to search for?")
        google().start_google(driver)
        while(1):
            print("I am listening")
            keyword2 = main().recognize_speech_from_mic(recognizer, microphone)
            if keyword2["transcription"]:
                break
            if not keyword2["success"]:
                break
            print("I didn't catch that. What did you say?\n")
        google().search_google(driver,keyword2["transcription"])
    elif "open youtube" in keyword["transcription"].lower():
        youtube().start_youtube(driver)
    elif "forward video" in keyword["transcription"].lower():
        youtube().fvideo(driver)
    elif "reverse video" in keyword["transcription"].lower():
        youtube().rvideo(driver)
    elif "search youtube" in keyword["transcription"].lower():
        print("What do want to search for?")
        while(1):
            print("I am listening")
            keyword2 = main().recognize_speech_from_mic(recognizer, microphone)
            if keyword2["transcription"]:
                break
            if not keyword2["success"]:
                break
            print("I didn't catch that. What did you say?\n")
        youtube().search_youtube(driver,keyword2["transcription"])
    elif "exit the browser" in keyword["transcription"].lower():
        common().quit(driver)
        break
