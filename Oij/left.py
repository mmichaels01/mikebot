import time
# Import the Raspberry Pi GPIO libraries that
# allow us to connect the Raspberry Pi to
# other physical devices via the General
# Purpose Input-Output (GPIO) pins
import RPi.GPIO as GPIO
import os


#Pin 12 for left wheel
LEFTWHEEL=12

GPIO.setwarnings(False)
GPIO.cleanup()

#Use the pin numbers on the GPIO to address the pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEFTWHEEL,GPIO.OUT)

try:
    while True:
        GPIO.output(LEFTWHEEL, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(LEFTWHEEL, GPIO.LOW)
        time.sleep(.5)
except KeyboardInterrupt:
    GPIO.output(LEFTWHEEL, GPIO.LOW)