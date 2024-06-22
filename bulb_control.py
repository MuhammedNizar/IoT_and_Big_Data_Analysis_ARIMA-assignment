import RPi.GPIO as GPIO
import time

# Define GPIO pins for the bulbs
BULB1_PIN = 17
BULB2_PIN = 27
BULB3_PIN = 22

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(BULB1_PIN, GPIO.OUT)
GPIO.setup(BULB2_PIN, GPIO.OUT)
GPIO.setup(BULB3_PIN, GPIO.OUT)

def set_bulbs(hi):
    GPIO.output(BULB1_PIN, GPIO.LOW)
    GPIO.output(BULB2_PIN, GPIO.LOW)
    GPIO.output(BULB3_PIN, GPIO.LOW)

    if hi <= 27:
        GPIO.output(BULB1_PIN, GPIO.HIGH) 
    elif hi <= 32:
        GPIO.output(BULB2_PIN, GPIO.HIGH)
    else:
        GPIO.output(BULB3_PIN, GPIO.HIGH) 

    
