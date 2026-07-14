import pyttsx3
import speech_recognition as sr


# Create voice engine

engine = pyttsx3.init()
engine.setProperty("rate",150) # speaking speed

voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)#female voice
# speak function
def speak(text):
    print("Aira:",text)
    engine.say(text)
    engine.runAndWait()
# listen function
def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening......") 
            recognizer.adjust_for_ambient_noise(source,duration=1)   
            audio = recognizer.listen(source)       
    
        command = recognizer.recognize_google(audio)
        print("You said:",command)
        return command.lower() 
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Speech recognition service error:", e)
        return ""
    
