from venv import logger

from flask import Flask, render_template, session
from flask_socketio import SocketIO, send, emit, disconnect

import speech_recognition as sr


from flask import request


app = Flask(__name__)
app.config["SECRET_KEY!"] = "slava_jesusu"
soketio = SocketIO(app)

datas = {}


@soketio.on("message")
def handle_message(message):
    datas[request.sid]["speech"].append(message)

@soketio.on("command")
def handle_command(message):

    emit("command_", b''.join(datas[request.sid]["speech"]))
    disconnect()

@soketio.on("connect") # в headers должны быть samples
def connect():
    datas[request.sid] = {"samples": int(request.headers["samples"]), "speech": []}





if __name__ == "__main__":
    soketio.run(app, host="0.0.0.0", allow_unsafe_werkzeug=True)