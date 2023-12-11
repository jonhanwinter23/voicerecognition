import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the speech recognition recognizer
r = sr.Recognizer()

# Khmer speech recognition function
def khmer_speech_recognition():
    with sr.Microphone() as source:
        print("សួស្តី!")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="km-KH")
            print("អ្នកបាននិយាយ:", text)
            return text
        except sr.UnknownValueError:
            print("មិនអាចស្វែងរកអត្ថបទទេ។")
            return None

def save_conversation(text):
    with open("conversation.txt", "a") as file:
        file.write(text + "\n")

def convert_text_to_speech(response):
    # Create a gTTS object with Khmer as the language
    tts = gTTS(text=response, lang='km')

    # Save the audio file
    tts.save("output.mp3")

    # Play the audio file
    os.system("afplay output.mp3")

# Read responses from a text file
def read_responses_from_file(filename):
    responses = {}
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        for line in lines:
            parts = line.split(":")
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                responses[key] = value
    return responses

# Responses dictionary
responses = read_responses_from_file("responses.txt.rtf")

# Khmer chatbot function
def khmer_chatbot():
    text = khmer_speech_recognition()
    if text is not None:
        save_conversation(text)
        response = responses.get(text)
        if response is not None:
            convert_text_to_speech(response)
        else:
            convert_text_to_speech("សូមសំអាត ខ្ញុំមិនអាចទំនាក់ទំនងបាននៅពេលនេះទេ។")
        print("ឆ្លើយ:", response)

# Main loop
while True:
    khmer_chatbot()