from venv import logger

from flask import Flask, render_template, session
from flask_socketio import SocketIO, send, emit, disconnect

import speech_recognition as sr
from speech_recognition import AudioData, AudioSource
from constans import FRT

from flask import request

app = Flask(__name__)
app.config["SECRET_KEY!"] = "slava_jesusu"
soketio = SocketIO(app)

datas = {}
recognize = sr.Recognizer(language="ru-RU")


@soketio.on("message")
def handle_message(message):
    datas[request.sid]["speech"].append(message)


@soketio.on("command")
def handle_command(message):
    a = AudioData(data=b''.join(datas[request.sid]["speech"]), rate=FRT)
    text = recognize.recognize(a)
    print(text)
    datas[request.sid]["speech"] = []


@soketio.on("connect")  # в headers должны быть samples
def connect():
    datas[request.sid] = {"samples": int(request.headers["samples"]), "speech": []}


@soketio.on("disconnect")
def disconnect():
    del datas[request.sid]


if __name__ == "__main__":
    soketio.run(app, host="0.0.0.0", allow_unsafe_werkzeug=True)
