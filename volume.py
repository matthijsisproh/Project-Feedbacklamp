#!/usr/bin/env python3
import RPi.GPIO as GPIO
from neopixel import *
import time

# LED CONFIGURATION
LED_COUNT = 32
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 20
LED_INVERT = False

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)


import sounddevice as sd
import numpy as np
import time

duration = 10  # seconds

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    strip.begin()
    strip.show()
    if int(volume_norm) >= 0 and int(volume_norm) < 10:
        strip.begin()
        strip.setPixelColor(0, Color(255, 0, 0))
        strip.setPixelColor(1, Color(255, 0, 0))
        strip.setPixelColor(2, Color(255, 0, 0))
        strip.setPixelColor(3, Color(255, 0, 0))
        strip.setPixelColor(4, Color(255, 0, 0))
        strip.setPixelColor(5, Color(255, 0, 0))
        strip.setPixelColor(6, Color(255, 0, 0))
        strip.setPixelColor(7, Color(255, 0, 0))
        strip.setPixelColor(8, Color(255, 0, 0))
        strip.setPixelColor(9, Color(255, 0, 0))
        strip.setPixelColor(10, Color(255, 0, 0))
        strip.setPixelColor(11, Color(255, 0, 0))
        strip.setPixelColor(12, Color(255, 0, 0))
        strip.setPixelColor(13, Color(255, 0, 0))
        strip.setPixelColor(14, Color(255, 0, 0))
        strip.setPixelColor(15, Color(255, 0, 0))
        strip.setPixelColor(16, Color(255, 0, 0))
        strip.setPixelColor(17, Color(255, 0, 0))
        strip.setPixelColor(18, Color(255, 0, 0))
        strip.setPixelColor(19, Color(255, 0, 0))
        strip.setPixelColor(20, Color(255, 0, 0))
        strip.setPixelColor(21, Color(255, 0, 0))
        strip.setPixelColor(22, Color(255, 0, 0))
        strip.setPixelColor(23, Color(255, 0, 0))
        strip.setPixelColor(24, Color(255, 0, 0))
        strip.setPixelColor(25, Color(255, 0, 0))
        strip.setPixelColor(26, Color(255, 0, 0))
        strip.setPixelColor(27, Color(255, 0, 0))
        strip.setPixelColor(28, Color(255, 0, 0))
        strip.setPixelColor(29, Color(255, 0, 0))
        strip.setPixelColor(30, Color(255, 0, 0))
        strip.setPixelColor(31, Color(255, 0, 0))
        strip.show()

    if int(volume_norm) >= 20 and int(volume_norm) < 50:
        strip.begin()
        strip.setPixelColor(0, Color(50, 205, 0))
        strip.setPixelColor(1, Color(50, 205, 0))
        strip.setPixelColor(2, Color(50, 205, 0))
        strip.setPixelColor(3, Color(50, 205, 0))
        strip.setPixelColor(4, Color(50, 205, 0))
        strip.setPixelColor(5, Color(50, 205, 0))
        strip.setPixelColor(6, Color(50, 205, 0))
        strip.setPixelColor(7, Color(50, 205, 0))
        strip.setPixelColor(8, Color(50, 205, 0))
        strip.setPixelColor(9, Color(50, 205, 0))
        strip.setPixelColor(10, Color(50, 205, 0))
        strip.setPixelColor(11, Color(50, 205, 0))
        strip.setPixelColor(12, Color(50, 205, 0))
        strip.setPixelColor(13, Color(50, 205, 0))
        strip.setPixelColor(14, Color(50, 205, 0))
        strip.setPixelColor(15, Color(50, 205, 0))
        strip.setPixelColor(16, Color(50, 205, 0))
        strip.setPixelColor(17, Color(50, 205, 0))
        strip.setPixelColor(18, Color(50, 205, 0))
        strip.setPixelColor(19, Color(50, 205, 0))
        strip.setPixelColor(20, Color(50, 205, 0))
        strip.setPixelColor(21, Color(50, 205, 0))
        strip.setPixelColor(22, Color(50, 205, 0))
        strip.setPixelColor(23, Color(50, 205, 0))
        strip.setPixelColor(24, Color(50, 205, 0))
        strip.setPixelColor(25, Color(50, 205, 0))
        strip.setPixelColor(26, Color(50, 205, 0))
        strip.setPixelColor(27, Color(50, 205, 0))
        strip.setPixelColor(28, Color(50, 205, 0))
        strip.setPixelColor(29, Color(50, 205, 0))
        strip.setPixelColor(30, Color(50, 205, 0))
        strip.setPixelColor(31, Color(50, 205, 0))
        strip.show()
    if int(volume_norm) >= 50:
        strip.begin()
        strip.setPixelColor(0, Color(0, 255, 0))
        strip.setPixelColor(1, Color(0, 255, 0))
        strip.setPixelColor(2, Color(0, 255, 0))
        strip.setPixelColor(3, Color(0, 255, 0))
        strip.setPixelColor(4, Color(0, 255, 0))
        strip.setPixelColor(5, Color(0, 255, 0))
        strip.setPixelColor(6, Color(0, 255, 0))
        strip.setPixelColor(7, Color(0, 255, 0))
        strip.setPixelColor(8, Color(0, 255, 0))
        strip.setPixelColor(9, Color(0, 255, 0))
        strip.setPixelColor(10, Color(0, 255, 0))
        strip.setPixelColor(11, Color(0, 255, 0))
        strip.setPixelColor(12, Color(0, 255, 0))
        strip.setPixelColor(13, Color(0, 255, 0))
        strip.setPixelColor(14, Color(0, 255, 0))
        strip.setPixelColor(15, Color(0, 255, 0))
        strip.setPixelColor(16, Color(0, 255, 0))
        strip.setPixelColor(17, Color(0, 255, 0))
        strip.setPixelColor(18, Color(0, 255, 0))
        strip.setPixelColor(19, Color(0, 255, 0))
        strip.setPixelColor(20, Color(0, 255, 0))
        strip.setPixelColor(21, Color(0, 255, 0))
        strip.setPixelColor(22, Color(0, 255, 0))
        strip.setPixelColor(23, Color(0, 255, 0))
        strip.setPixelColor(24, Color(0, 255, 0))
        strip.setPixelColor(25, Color(0, 255, 0))
        strip.setPixelColor(26, Color(0, 255, 0))
        strip.setPixelColor(27, Color(0, 255, 0))
        strip.setPixelColor(28, Color(0, 255, 0))
        strip.setPixelColor(29, Color(0, 255, 0))
        strip.setPixelColor(30, Color(0, 255, 0))
        strip.setPixelColor(31, Color(0, 255, 0))
        strip.show()



with sd.Stream(callback=print_sound):
    while True:
        sd.sleep(duration * 1)
        time.sleep(1)