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
GPIO.cleanup()
# Set up the GPIO library to use Raspberry Pi
# board pin numbers
GPIO.setmode(GPIO.BOARD)
# Set Pin 3 on the GPIO header to act as
# an output
# Assign RED, YELLOW, GREEN, BLUE to pins 3, 5, 7, 11 respectively
DELAY=.02
RED=3
YELLOW=5
GREEN=7
BLUE=11
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(RED,GPIO.LOW)
GPIO.output(YELLOW,GPIO.LOW)
GPIO.output(GREEN,GPIO.LOW)
GPIO.output(BLUE,GPIO.LOW)
count=0
try:
	while count < 10:
		time.sleep(DELAY)
		# Turn on the red LED
		GPIO.output(RED,GPIO.HIGH)
		time.sleep(DELAY)
		# Turn off the red LED
		GPIO.output(RED,GPIO.LOW)
		time.sleep(DELAY)
		# Turn on the yellow LED
		GPIO.output(YELLOW,GPIO.HIGH)
		time.sleep(DELAY)
		# Turn off the yellow LED
		GPIO.output(YELLOW,GPIO.LOW)
		time.sleep(DELAY)
		# Turn on the green LED
		GPIO.output(GREEN,GPIO.HIGH)
		time.sleep(DELAY)
		# Turn off the green LED
		GPIO.output(GREEN,GPIO.LOW)
		time.sleep(DELAY)
		# Turn on the blue LED
		GPIO.output(BLUE,GPIO.HIGH)
		time.sleep(DELAY)
		# Turn off the blue LED
		GPIO.output(BLUE,GPIO.LOW)
		count = count + 1
except KeyboardInterrupt:
	#call("echo Hello World", shell=True)
	print "Hit interrupt."
	import os
	cmd = '/home/pi/bin/lo'
	os.system(cmd)
	#GPIO.output(3,GPIO.LOW)
	#GPIO.output(YELLOW,GPIO.LOW)
	#GPIO.output(GREEN,GPIO.LOW)
	#GPIO.output(BLUE,GPIO.LOW)
	#GPIO.cleanup()
