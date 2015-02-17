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
DELAY=3
LIGHT=3
GPIO.setup(LIGHT,GPIO.OUT)
GPIO.output(LIGHT,GPIO.LOW)
try:
	while True:
		time.sleep(DELAY)
		# Turn on the LIGHT LED
		GPIO.output(LIGHT,GPIO.HIGH)
		print "Turned on the LED."
		time.sleep(DELAY)
		# Turn off the LIGHT LED
		GPIO.output(LIGHT,GPIO.LOW)
		print "Turned off the LED."
except KeyboardInterrupt:
	#call("echo Hello World", shell=True)
	print "Please, oh please let me keep flashing."
	import os
	cmd = '/home/pi/bin/lo'
	os.system(cmd)
	GPIO.cleanup()
