import sounddevice as sd
import numpy as np
import time

duration = 10  # seconds

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    if int(volume_norm) >= 0 and int(volume_norm) < 10:
        print("Groen!")

    if int(volume_norm) >= 20 and int(volume_norm) < 50:
        print("Oranje!")

    if int(volume_norm) >= 50:
        print("Rood!")

with sd.Stream(callback=print_sound):
    while True:
        sd.sleep(duration * 1)
        time.sleep(1)