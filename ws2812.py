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
strip.begin()
strip.show()


while 1:
	strip.begin()
	strip.setPixelColor(0, Color(70,185,0))
	strip.setPixelColor(1, Color(70,185,0))
	strip.setPixelColor(2, Color(70,185,0))
	strip.setPixelColor(3, Color(70,185,0))
	strip.setPixelColor(4, Color(70,185,0))
	strip.setPixelColor(5, Color(70,185,0))
	strip.setPixelColor(6, Color(70,185,0))
	strip.setPixelColor(7, Color(70,185,0))
	strip.setPixelColor(8, Color(70,185,0))
	strip.setPixelColor(9, Color(70,185,0))
	strip.setPixelColor(10, Color(70,185,0))
	strip.setPixelColor(11, Color(70,185,0))
	strip.setPixelColor(12, Color(70,185,0))
	strip.setPixelColor(13, Color(70,185,0))
	strip.setPixelColor(14, Color(70,185,0))
	strip.setPixelColor(15, Color(70,185,0))
	strip.setPixelColor(16, Color(70,185,0))
	strip.setPixelColor(17, Color(70,185,0))
	strip.setPixelColor(18, Color(70,185,0))
	strip.setPixelColor(19, Color(70,185,0))
	strip.setPixelColor(20, Color(70,185,0))
	strip.setPixelColor(21, Color(70,185,0))
	strip.setPixelColor(22, Color(70,185,0))
	strip.setPixelColor(23, Color(70,185,0))
	strip.setPixelColor(24, Color(70,185,0))
	strip.setPixelColor(25, Color(70,185,0))
	strip.setPixelColor(26, Color(70,185,0))
	strip.setPixelColor(27, Color(70,185,0))
	strip.setPixelColor(28, Color(70,185,0))
	strip.setPixelColor(29, Color(70,185,0))
	strip.setPixelColor(30, Color(70,185,0))
	strip.setPixelColor(31, Color(70,185,0))

        strip.show()
        time.sleep(0.1)
