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
# Assign BLUE, GREEN, RED to pins 16, 18, 22 respectively
DELAY=.5
BLUE=11
GREEN=13
RED=15
GPIO.setup(BLUE,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)
GPIO.output(BLUE,GPIO.LOW)
GPIO.output(GREEN,GPIO.LOW)
GPIO.output(RED,GPIO.LOW)
try:
	while True:
		#time.sleep(DELAY)
		# Turn on the blue LED
		GPIO.output(BLUE,GPIO.HIGH)
		time.sleep(DELAY)
		# Turn off the blue LED
		GPIO.output(BLUE,GPIO.LOW)
		time.sleep(DELAY)
		# Turn on the green LED
		GPIO.output(GREEN,GPIO.HIGH)
		time.sleep(DELAY)
		# Turn off the green LED
		GPIO.output(GREEN,GPIO.LOW)
		time.sleep(DELAY)
		# Turn on the red LED
		GPIO.output(RED,GPIO.HIGH)
		time.sleep(DELAY)
		# Turn off the red LED
		GPIO.output(RED,GPIO.LOW)
		time.sleep(DELAY)
except KeyboardInterrupt:
	#call("echo Hello World", shell=True)
	print "\n\nOh please let me keep flashing!!!"
	import os
	cmd = '/home/pi/bin/lo'
	os.system(cmd)
