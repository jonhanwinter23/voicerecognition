import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer
r = sr.Recognizer()

# Initialize the speech synthesis engine
engine = pyttsx3.init()

# Define the dictionary of responses
responses = {
    "hello": "Hi Sam, how are you?",
    "I'm good": "I'm totally fine.",
    "I am good": "I'm totally fine.",
    "can you help me with something": "For sure Sam, I can help you with anything"
}

def listen_and_respond():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        # Use Google Speech Recognition to convert speech to text
        text = r.recognize_google(audio)
        print("You said:", text)

        # Process user's input using the dictionary
        response = responses.get(text, "Sorry, I didn't get that.")

        print("Chatbot:", response)

        # Convert the response text to speech
        engine.say(response)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Start the conversation
while True:
    listen_and_respond()