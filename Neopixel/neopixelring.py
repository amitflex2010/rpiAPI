# Demoscript NeoPixel Ring (12 led)
# https://raspberrytips.nl

import time

from neopixel import *
from random import randint

LEDS        = 7     # Aantel LEDS
PIN         = 18     # GPIO 18 / PIN 12
BRIGHTNESS  = 55     # min 0 / max 255

KLEUR_R     = 255
KLEUR_G     = 0
KLEUR_B     = 0

LED_1_COUNT      = 30      # Number of LED pixels.
LED_1_PIN        = 18      # GPIO pin connected to the pixels (must support PWM! GPIO 13 and 18 on RPi 3).
LED_1_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_1_DMA        = 10      # DMA channel to use for generating signal (Between 1 and 14)
LED_1_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
LED_1_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_1_CHANNEL    = 0       # 0 or 1
LED_1_STRIP      = ws.SK6812_STRIP_GRBW

def loopLed(ring, color, wait_ms):

       for i in range(strip1.numPixels()):
	   if i % 2:
                # even number
                strip1.setPixelColor(i, color1)
                strip1.show()
                time.sleep(wait_ms/1000.0)
           else:
                # odd number
                strip1.setPixelColor(i, color1)
                strip1.show()
                time.sleep(wait_ms/1000.0)
	        time.sleep(1)

def blackout(strip):
	for i in range(max(strip1.numPixels(), strip1.numPixels())):
	    strip.setPixelColor(i, Color(0,0,0))
	    strip.show()

if __name__ == '__main__':

        ring = Adafruit_NeoPixel(LED_1_COUNT, LED_1_PIN, LED_1_FREQ_HZ, LED_1_DMA, LED_1_INVERT, LED_1_BRIGHTNESS, LED_1_CHANNEL, LED_1_STRIP)

        ring.begin()
        

        blackout(ring) 
    
        loopLed (ring, Color(KLEUR_G, KLEUR_R, KLEUR_B),100)
        #loopLed(ring, Color(0,255,0),100)
        #loopLed(ring, Color(0,255,255),100)
        #loopLed(ring, Color(0,255,255),100)
           # resetLeds (ring,Color(0,0,0))
