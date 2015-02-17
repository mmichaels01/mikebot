import time
# Import the Raspberry Pi GPIO libraries that
# allow us to connect the Raspberry Pi to
# other physical devices via the General
# Purpose Input-Output (GPIO) pins
import RPi.GPIO as GPIO
import os
GPIO.setwarnings(False)
# Now we need to set-up the General Purpose
# Input-Ouput (GPIO) pins
# Clear the current set-up so that we can
# start from scratch
GPIO.cleanup()
# Set up the GPIO library to use Raspberry Pi
# board pin numbers
GPIO.setmode(GPIO.BOARD)
# Set Pin 16 on the GPIO header to act as
# the output port to control forward movement on RIGHTWHEEL
#LIGHT=15
OFFDELAY=.05
ONDELAY=.1
RIGHTWHEEL=16
LEFTWHEEL=12
#GPIO.setup(LIGHT,GPIO.OUT)
GPIO.setup(RIGHTWHEEL,GPIO.OUT)
GPIO.setup(LEFTWHEEL,GPIO.OUT)
#GPIO.output(LIGHT,GPIO.LOW)
GPIO.output(RIGHTWHEEL,GPIO.LOW)
GPIO.output(LEFTWHEEL,GPIO.LOW)
#cmd = 'mpg123 /home/pi/sounds/Be*.mp3 > /dev/null 2>/dev/null &'
#os.system(cmd)

try:
    while True:
		time.sleep(OFFDELAY)
		GPIO.output(RIGHTWHEEL,GPIO.HIGH)
		#GPIO.output(LEFTWHEEL,GPIO.HIGH)
		#GPIO.output(LIGHT,GPIO.HIGH)
		time.sleep(ONDELAY)
		GPIO.output(RIGHTWHEEL,GPIO.LOW)
		#GPIO.output(LEFTWHEEL,GPIO.LOW)
		#GPIO.output(LIGHT,GPIO.LOW)
except KeyboardInterrupt:
	#call("echo Hello World", shell=True)
	print "Please, oh please let me keep moving."
	GPIO.output(RIGHTWHEEL,GPIO.LOW)
	GPIO.output(LEFTWHEEL,GPIO.LOW)
	import os
	cmd = '/home/pi/bin/lo'
	os.system(cmd)
