import webbrowser
import datetime
import subprocess
import pyjokes
import urllib.parse
def open_google():
    webbrowser.open("https://www.google.com/")
    return "Opening Google"    

def open_youtube():
    webbrowser.open("https://www.youtube.com/")
    return "Opening YouTube"

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return f"The Current time is {current_time}"

def get_date():
    today = datetime.datetime.now().strftime("%d %B %Y")
    return f"Today's date is {today}"

def tell_joke():
    joke= pyjokes.get_joke()
    return joke

def open_calculator():
    subprocess.Popen("Calc")
    return "Opening Calculator"

def play_song(song_name):
    if song_name.strip() == "":  
        return "No song name provided"
    print(f"playing {song_name} on YouTube.")
    query = urllib.parse.quote(song_name)
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    return f"playing {song_name}"

def open_notepad():
    subprocess.Popen("notepad")
    return "Opening Notepad"

def open_camera():
    subprocess.Popen("start microsoft.windows.camera:",shell=True)
    return "Opening Camera"

def open_whatsapp():
    webbrowser.open("https://web.whatsapp.com/")
    return "WhatsApp is opened"

def search_google(query):
    if query.strip() == "":
        print(f"Searching Google for {query}")
        search_url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
        webbrowser.open(search_url)
    return "Please tell me what to search"    
    
