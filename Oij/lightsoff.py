import time
# Import the Raspberry Pi GPIO libraries that
# allow us to connect the Raspberry Pi to
# other physical devices via the General
# Purpose Input-Output (GPIO) pins
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
# Now we need to set-up the General Purpose
# Input-Ouput (GPIO) pins
# Clear the current set-up so that we can
# start from scratch
# Set up the GPIO library to use Raspberry Pi
# board pin numbers
GPIO.setmode(GPIO.BOARD)
# Set Pin 3 on the GPIO header to act as
# an output
# Assign RED, YELLOW, GREEN, BLUE to pins 3, 5, 7, 11 respectively
#RED=3
#YELLOW=5
#GREEN=7
#BLUE=11
LIGHT=23
#GPIO.setup(RED,GPIO.OUT)
#GPIO.setup(YELLOW,GPIO.OUT)
#GPIO.setup(GREEN,GPIO.OUT)
#GPIO.setup(BLUE,GPIO.OUT)
GPIO.setup(LIGHT,GPIO.OUT)

#GPIO.output(RED,GPIO.LOW)
#GPIO.output(YELLOW,GPIO.LOW)
#GPIO.output(GREEN,GPIO.LOW)
#GPIO.output(BLUE,GPIO.LOW)
GPIO.output(LIGHT,GPIO.LOW)

GPIO.cleanup()
