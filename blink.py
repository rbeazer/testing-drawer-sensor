#!/usr/bin/python
def blinkLED():
    import RPi.GPIO as GPIO
    import time

    # Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
    GPIO.setmode(GPIO.BCM)

    red_pin = 18

    GPIO.setup(red_pin, GPIO.OUT)


    try:         
        while True:
            GPIO.output(red_pin, True)  # LED on
            time.sleep(0.5)             # delay 0.5 seconds
            GPIO.output(red_pin, False) # LED off
            time.sleep(0.5)             # delay 0.5 seconds
    finally:  
        GPIO.cleanup()

####################################################
####################################################

import time
import RPi.GPIO as GPIO
import requests
GPIO.setmode(GPIO.BCM)
GPIO.setWarnings(False)

doorPin = 23

GPIO.setup(doorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

try:
    while True:
        if GPIO.input(doorPin):
            print("Door Alarm!")
            r= requests.post('https://maker.ifttt.com/trigger/drawerOpen/with/key/ctqMix_lSYsuoam_Kw6DLB', params={"value1":"none","value2":"none","value3":"none"})
            blinkLED()

        time.sleep(1)

except KeyboardInterrupt:
    print("Quit")
    
###########################################
############################################




