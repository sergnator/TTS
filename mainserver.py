from flask import Flask, render_template, session
from flask_socketio import SocketIO, send, emit, disconnect

from vosk import KaldiRecognizer, Model

from constans import FRT
import json
from flask import request

app = Flask(__name__)
app.config["SECRET_KEY!"] = "slava_jesusu"
soketio = SocketIO(app)

datas = {}
model = Model(model_path="/vosk-model-ru-0.42.zip")


@soketio.on("message")
def handle_message(message):
    datas[request.sid]["speech"].append(message)


@soketio.on("command")
def handle_command(message):
    offline_recognizer = KaldiRecognizer(model, FRT)
    offline_recognizer.AcceptWaveform(datas[request.sid]["speech"])
    text = json.loads(offline_recognizer.Result())["text"]
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
