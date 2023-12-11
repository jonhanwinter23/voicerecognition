import speech_recognition as sr
from gtts import gTTS
import os
import responses

class KhmerChatbot:
    def __init__(self):
        self.responses = responses.responses
        self.r = sr.Recognizer()

    def khmer_speech_recognition(self):
        with sr.Microphone() as source:
            print("សួស្តី!")
            audio = self.r.listen(source)

            try:
                text = self.r.recognize_google(audio, language="km-KH")
                print("អ្នកបាននិយាយ:", text)
                return text
            except sr.UnknownValueError:
                print("មិនអាចស្វែងរកអត្ថបទទេ។")
                return None

    def convert_text_to_speech(self, response):
        tts = gTTS(text=response, lang='km')
        tts.save("output.mp3")
        os.system("afplay output.mp3")

    def khmer_chatbot(self):
        text = self.khmer_speech_recognition()
        if text is not None:
            response = self.responses.get(text)
            if response is not None:
                self.convert_text_to_speech(response)
            else:
                self.convert_text_to_speech("សូមនិយាយម្តងទៀតបានទេ!")
            print("ឆ្លើយ:", response)

    def run(self):
        while True:
            self.khmer_chatbot()

# Instantiate the KhmerChatbot class and run the chatbot
chatbot = KhmerChatbot()
chatbot.run(run)