#Python 2.7.6
#RestfulClient.py

import requests
from requests.auth import HTTPDigestAuth
import json
import sched, time
import threading 


from neopixel import *
from random import randint

LEDS        = 7     # Aantel LEDS
PIN         = 18     # GPIO 18 / PIN 12
BRIGHTNESS  = 55     # min 0 / max 255

KLEUR_R     = 0
KLEUR_G     = 255
KLEUR_B     = 0


# Replace with the correct URL
url = "https://us-central1-mysampleproject-3b9ff.cloudfunctions.net/nodeapp/getContacts"

def loopLed(ring, color, wait_ms):

        for i in range(ring.numPixels()):
                ring.setPixelColor(i,color)
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

def pollEndPoint(sc):

        myResponse = requests.get(url)
        # For successful API call, response code will be 200 (OK)
        if(myResponse.ok):
        # Loading the response data into a dict variable
	# json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
	    jData = json.loads(myResponse.content)
            print(jData)
            resetLeds (ring,Color(0,0,0))    
            loopLed (ring, Color(KLEUR_G, 0, 0),100)
        else:
        # If response code is not ok (200), print the resulting http error code with description
            resetLeds (ring,Color(0,0,0))
    	    loopLed (ring, Color(0, KLEUR_R, 0),100)
	    myResponse.raise_for_status()

        s.enter(10,1, pollEndPoint, (sc,))    
    
ring = Adafruit_NeoPixel(LEDS , PIN , 800000 , 7 , False , BRIGHTNESS)
ring.begin()
s = sched.scheduler(time.time, time.sleep)
s.enter(10, 1, pollEndPoint, (s,))
s.run()


	
