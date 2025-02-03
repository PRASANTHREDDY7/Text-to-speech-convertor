import pyttsx3

engine = pyttsx3.init()  #to initialize the pyttsx3
engine.setProperty('rate', 100) # speed controller
engine.setProperty('volume',2) # volume adujuster
voices = engine.getProperty('voices')  # voice changer
engine.setProperty('voice', voices[1].id)  # For female voice
def speak_text(text):
    engine.say(text)  
    engine.runAndWait()  


text_input = input("Enter the text you want to convert to speech: ")

speak_text(text_input) 

