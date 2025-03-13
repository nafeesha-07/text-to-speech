import pyttsx3

text_speech = pyttsx3.init()

# Get available voices
voices = text_speech.getProperty('voices')

# for tone 
text_speech.setProperty('voice',voices[1].id)
text_speech.say(input("Enter Text: "))

text_speech.runAndWait()
