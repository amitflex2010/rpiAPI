#Python 2.7.6
#RestfulClient.py

import requests
from requests.auth import HTTPDigestAuth
import json
import sched, time
import threading 
import sys


from neopixel import *
from random import randint

LEDS        = 12     # Aantel LEDS
PIN         = 18     # GPIO 18 / PIN 12
BRIGHTNESS  = 55     # min 0 / max 255

KLEUR_R     = 255
KLEUR_G     = 255
KLEUR_B     = 0

LED_1_COUNT      = 7      # Number of LED pixels.
LED_1_PIN        = 18      # GPIO pin connected to the pixels (must support PWM! GPIO 13 and 18 on RPi 3).
LED_1_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_1_DMA        = 10      # DMA channel to use for generating signal (Between 1 and 14)
LED_1_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
LED_1_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_1_CHANNEL    = 0       # 0 or 1
LED_1_STRIP      = ws.SK6812_STRIP_GRBW

LED_2_COUNT      = 7      # Number of LED pixels.
LED_2_PIN        = 13      # GPIO pin connected to the pixels (must support PWM! GPIO 13 and 18 on RPi 3).
LED_2_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_2_DMA        = 10      # DMA channel to use for generating signal (Between 1 and 14)
LED_2_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
LED_2_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_2_CHANNEL    = 0       # 0 or 1
LED_2_STRIP      = ws.SK6812_STRIP_GRBW



# Replace with the correct URL
UTE3_URL = "https://api-dashboard-ite.klm.com/api/postman/flows?envName=ute3&&isFlow=false"
UTE1_URL = "https://api-dashboard-ite.klm.com/api/postman/flows?envName=ute1&&isFlow=false"

def loopLed(strip1, color1, wait_ms):

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


def blackout(strip1):
	for i in range(max(strip1.numPixels(), strip1.numPixels())):
	    strip1.setPixelColor(i, Color(0,0,0))
	    strip1.show()


def pollEndPoint(sc):
        pollUte3()
        pollUte1()
        s.enter(10,1, pollEndPoint, (sc,))   

def pollUte1():
        try:
            ute1Response = requests.get(UTE1_URL)
        
        # For successful API call, response code will be 200 (OK)
    
            if(ute1Response.ok):
        # Loading the response data into a dict variable
	# json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
                jData = json.loads(ute1Response.content)
                print('data')
                blackout(ring2)
                loopLed (ring2, Color(0, KLEUR_G, 0),100)
                for item in jData["stepDetails"]:   
                        if item['servicename'] == "BRE" and item['status'] == "FAIL"  :
                            print item['status']
                            blackout(ring2) 
                            loopLed (ring2, Color(KLEUR_R, 0, 0),100)    

                pass
            else:
        # If response code is not ok (200), print the resulting http error code with description
                print(ute1Response.status_code)
                blackout(ring2) 
                loopLed (ring2, Color(KLEUR_R, 0, 0),100)
                # myResponse.raise_for_status()
        except requests.exceptions.ConnectionError as errc:
            blackout(ring2) 
            loopLed (ring2, Color(KLEUR_R, 0, 0),100)    
            print ("Http Error:",errc)
            sys.exit(1)


def pollUte3():
        try:
            ute3Response = requests.get(UTE3_URL)
        
        # For successful API call, response code will be 200 (OK)
    
            if(ute3Response.ok):
        # Loading the response data into a dict variable
	# json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
                jData = json.loads(ute3Response.content)
                print('data')
                blackout(ring1)
                loopLed (ring1, Color(0, KLEUR_G, 0),100)
                for item in jData["stepDetails"]:   
                        if item['servicename'] == "BRE" and item['status'] == "FAIL"  :
                            print item['status']
                            blackout(ring1) 
                            loopLed (ring1, Color(KLEUR_R, 0, 0),100)    

                pass
            else:
        # If response code is not ok (200), print the resulting http error code with description
                print(ute3Response.status_code)
                blackout(ring1) 
                loopLed (ring1, Color(KLEUR_R, 0, 0),100)
                # myResponse.raise_for_status()
        except requests.exceptions.ConnectionError as errc:
            blackout(ring1) 
            loopLed (ring1, Color(KLEUR_R, 0, 0),100)    
            print ("Http Error:",errc)
            sys.exit(1)        
    
def initialSetup():
        pollUte3()
        pollUte1()
                    


ring1 = Adafruit_NeoPixel(LED_1_COUNT, LED_1_PIN, LED_1_FREQ_HZ, LED_1_DMA, LED_1_INVERT, LED_1_BRIGHTNESS, LED_1_CHANNEL, LED_1_STRIP)
ring2 = Adafruit_NeoPixel(LED_2_COUNT, LED_2_PIN, LED_2_FREQ_HZ, LED_2_DMA, LED_2_INVERT, LED_2_BRIGHTNESS, LED_2_CHANNEL, LED_2_STRIP)
ring1.begin()
ring2.begin()
initialSetup()
s = sched.scheduler(time.time, time.sleep)
s.enter(10, 1, pollEndPoint, (s,))
s.run()


	
