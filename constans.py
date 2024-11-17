import pyaudio

CHUNK = 1024
FRT = pyaudio.paInt16
CHAN = 1
RT = 44100
REC_SEC = 20
OUTPUT = "output.wav"