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

def loopLed(ring, color, wait_ms):

       # for i in range(ring.numPixels()):
        ring.setPixelColor(0,Color(KLEUR_G, KLEUR_R, KLEUR_B))
        ring.show()
        time.sleep(wait_ms/1000.0)
        ring.setPixelColor(1,Color(KLEUR_G, KLEUR_R, KLEUR_B))
        ring.show()
        time.sleep(wait_ms/1000.0)
        ring.setPixelColor(2,Color(KLEUR_G, KLEUR_R, KLEUR_B))
        ring.show()
        time.sleep(wait_ms/1000.0)
        ring.setPixelColor(3,Color(KLEUR_G, KLEUR_R, KLEUR_B))
        ring.show()
        time.sleep(wait_ms/1000.0)
               # ring.setPixelColor(i,0)
               # ring.setPixelColor(i-1,0)

       # for i in range(ring.numPixels()-1,-1,-1):
               # ring.setPixelColor(i,color)
                # ring.show()
          #      time.sleep(wait_ms/1000.0)
           #     ring.setPixelColor(i,0)
            #    ring.setPixelColor(i+1,0)

def resetLeds(ring, color, wait_ms=10):

        for i in range(ring.numPixels()):
                ring.setPixelColor(i, color)
                ring.show()

if __name__ == '__main__':

        ring = Adafruit_NeoPixel(LEDS , PIN , 800000 , 7 , False , BRIGHTNESS)

        ring.begin()
        

       # loopLed(ring, Color(0,0,0),1000) 
    
        loopLed (ring, Color(KLEUR_G, KLEUR_R, KLEUR_B),100)
        #loopLed(ring, Color(0,255,0),100)
        #loopLed(ring, Color(0,255,255),100)
        #loopLed(ring, Color(0,255,255),100)
           # resetLeds (ring,Color(0,0,0))
