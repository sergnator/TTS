from flask import Flask, render_template
from flask_socketio import SocketIO, send

import speech_recognition as sr
import wave
import sys
import pyaudio
from speech_recognition import AudioData

CHUNK = 1024
FRT = pyaudio.paInt16
CHAN = 1
RT = 44100
REC_SEC = 5
OUTPUT = "output1.wav"

frames = []
app = Flask(__name__)
app.config["SECRET_KEY!"] = "slava_jesusu"
soketio = SocketIO(app)
recognizer = sr.Recognizer()
sr.LANGUAGE = 'ru-RU'
big_text = None
@soketio.on("message")
def handle_message(message):
    global big_text
    frames.append(message["data"])
    try:
        audio_data = AudioData(b''.join(frames), RT , message["samples"])

        text = recognizer.recognize_google(audio_data, language='ru-RU')
        if text != big_text:
            print(text)
            big_text = text
    except:
        pass



if __name__ == "__main__":
    soketio.run(app, host="0.0.0.0", allow_unsafe_werkzeug=True)