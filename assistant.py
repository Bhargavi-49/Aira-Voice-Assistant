from utils import clean_command
from commands import (open_google,open_youtube,get_time,get_date,tell_joke,open_calculator,play_song,open_notepad,open_camera,open_whatsapp,search_google)
from config import EXIT_COMMANDS
def process_command(command):
    command = clean_command(command)
    if "open google" in command  or "open_google" in command:
        return open_google()
    
    elif "open youtube" in command or "open_youtube" in command:
        return open_youtube()
    
    elif command.startswith("play "):
        song_name = command.replace("play", "",1).strip()
        return play_song(song_name)
    
    elif "time" in command:
        return get_time()
    
    elif "date" in command:
        return get_date()
    
    elif "joke" in command:
        return tell_joke()
    
    elif "calculator" in command:
        return open_calculator()
    
    elif "open notepad" in command:
        return open_notepad()
    
    elif "open camera" in command:
        return open_camera()
    
    elif "open whatsapp" in command:
        return open_whatsapp()
    
    elif command.startswith("search google"):
        query = command.replace("search google","",1).strip()
        return search_google(query)
    
    elif command in EXIT_COMMANDS:
        return "exit"
    
    else:
        return "Sorry, I didn't understand that command."
    