from time import sleep

from constans import *
import socketio

p = pyaudio.PyAudio()

client = socketio.Client()

@client.on("command_")
def do_command():
    print('afsgasg')




client.connect("http://192.168.68.105:5000", headers={"samples": str(p.get_sample_size(FRT))})

out = p.open(format=FRT, channels=CHAN, rate=RT, output=True)

stream = p.open(format=FRT, channels=CHAN, rate=RT, input=True, frames_per_buffer=CHUNK)  # открываем поток для записи
print("rec")
for i in range(0, int(RT / CHUNK * REC_SEC)):
    data = stream.read(CHUNK)
    client.emit("message", data)
print("stop")
stream.close()
client.emit("command", "алёёёёёёёёёёёёёёёёёёёёёёёёёёёёёёёёёёёёёёёё")
client.sleep(5)

