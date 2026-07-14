
# Aira - Voice Assistant

## Description

**Aira** is a Python-based voice assistant that listens to user commands, processes them, and performs various tasks such as opening websites, telling the current time and date, searching Google, opening system applications, playing songs on YouTube, and telling jokes.

The project uses **Speech Recognition** to understand voice commands and **Text-to-Speech (TTS)** to respond to the user, providing an interactive voice-controlled experience.



## Features

* Voice-controlled assistant
* Text-to-Speech responses
* Speech Recognition using a microphone
* Open Google
* Open YouTube
* Search Google
* Play songs on YouTube
* Tell the current time
* Tell the current date
* Tell random jokes
* Open Calculator
* Open Notepad
* Open Camera
* Open WhatsApp Web
* Exit using voice commands such as **exit**, **quit**, **stop**, or **bye**

---

## Project Structure

```text
Aira-Voice-Assistant/
│── app.py
│── assistant.py
│── commands.py
│── speech.py
│── utils.py
│── config.py
│── README.md
```

---

## Technologies Used

* Python 3
* SpeechRecognition
* pyttsx3
* PyAudio
* pyjokes
* webbrowser
* subprocess
* datetime
* urllib

---

## Requirements

Install all required libraries before running the project.

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
pip install pyjokes
```

---

## File Description

### `app.py`

* Starts the voice assistant.
* Greets the user.
* Continuously listens for commands.
* Sends commands to the command processor.
* Stops when the user says an exit command.

### `assistant.py`

* Processes voice commands.
* Identifies which command the user requested.
* Calls the appropriate function from `commands.py`.

### `commands.py`

Contains all assistant actions such as:

* Open Google
* Open YouTube
* Search Google
* Play songs
* Open Calculator
* Open Notepad
* Open Camera
* Open WhatsApp
* Tell jokes
* Get current time
* Get current date

### `speech.py`

Handles:

* Text-to-Speech using **pyttsx3**
* Speech Recognition using Google's Speech Recognition API
* Microphone input

### `utils.py`

Contains helper functions for cleaning and formatting user commands.

### `config.py`

Stores configuration values such as:

* Assistant name
* Exit commands

---

## Algorithm

### Step 1

Start the application.

### Step 2

Initialize the Text-to-Speech engine.

### Step 3

Greet the user using the assistant name stored in `config.py`.

### Step 4

Listen for a voice command through the microphone.

### Step 5

Convert speech into text using Google Speech Recognition.

### Step 6

Clean the command using `utils.py`.

### Step 7

Match the command with available actions.

Examples:

* Open Google
* Open YouTube
* Search Google
* Play a song
* Open Calculator
* Open Notepad
* Open Camera
* Open WhatsApp
* Tell a joke
* Get time
* Get date

### Step 8

Execute the requested task.

### Step 9

Wait for the next command.

### Step 10

If the user says:

* exit
* quit
* stop
* bye

Terminate the assistant.

---

## Supported Voice Commands

| Command              | Action                                 |
| -------------------- | -------------------------------------- |
| Open Google          | Opens Google                           |
| Open YouTube         | Opens YouTube                          |
| Search Google Python | Searches Google for Python             |
| Play Believer        | Searches and plays the song on YouTube |
| Time                 | Tells the current time                 |
| Date                 | Tells today's date                     |
| Joke                 | Tells a random joke                    |
| Open Calculator      | Opens Calculator                       |
| Open Notepad         | Opens Notepad                          |
| Open Camera          | Opens Camera                           |
| Open WhatsApp        | Opens WhatsApp Web                     |
| Exit                 | Closes the assistant                   |



## Sample Output


https://github.com/user-attachments/assets/90e8d802-147a-4857-86bf-9c0518b5c972



## Note

* A microphone is required for voice input.
* An internet connection is required for Speech Recognition and Google searches.
* The project is currently optimized for Windows because it opens Windows applications such as Calculator, Camera, and Notepad.
* The assistant currently supports English voice commands.


## Author

**Bhargavi**
