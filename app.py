from assistant import process_command
from speech import speak,listen
from config import ASSISTANT_NAME

def main():
    speak(f"Hello! I am {ASSISTANT_NAME} how can i help you?")
    while True:
        command = listen()
        if command == "":
            speak("Sorry, I didn't catch that")
            continue
        response = process_command(command)
        print("Response from assistant:",response)

        if response == "exit":
            print("Goodbye")
            break
        
main()        