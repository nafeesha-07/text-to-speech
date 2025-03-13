# Text-to-Speech Converter using Python

This is a simple *Text-to-Speech (TTS)* converter using Python's pyttsx3 library. It allows users to input text, which is then converted into speech.

## Features

- Converts user input text to speech.
- Uses system voices (male/female) for speech synthesis.
- Works offline without an internet connection.

## Prerequisites

- Python 3.x installed on your system.
- Install the required library:

  ```bash
  pip install pyttsx3

How to Run

1. Clone this repository or download the texttospeech.py file.


2. Open a terminal or command prompt in the project directory.


3. Run the script:

    python texttospeech.py


4. Enter the text when prompted, and the program will convert it to speech.

Code Explanation

The Python script performs the following steps:

1. Initialize the pyttsx3 engine

2. Retrieve available voices on the system.

3. Set a voice (default is voices[0], change to voices[1] for a different voice).

4. Take user input and convert it to speech.


 Customization

Change Voice: Modify voices[0].id to voices[1].id for an alternative voice.

 Adjust Speech Rate:

text_speech.setProperty('rate', 150)  # Default is around 200

 Modify Volume:

text_speech.setProperty('volume', 1.0)  # Range: 0.0 to 1.0


License

This project is open-source and free to use.




# Author
Nafeesha
