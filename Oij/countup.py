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
# Assign ONES, TWOS, FOURS, EIGHTS to pins 3, 5, 7, 11 respectively
DELAY=.7
ONES=11
TWOS=7
FOURS=5
EIGHTS=3
GPIO.setup(ONES,GPIO.OUT)
GPIO.setup(TWOS,GPIO.OUT)
GPIO.setup(FOURS,GPIO.OUT)
GPIO.setup(EIGHTS,GPIO.OUT)
try:
	while True:
		GPIO.output(ONES,GPIO.LOW)
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.LOW)
		print "ZERO"
		time.sleep(DELAY)
		GPIO.output(ONES,GPIO.HIGH) #1
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.LOW)
		print "ONE"
		time.sleep(DELAY)
		GPIO.output(ONES,GPIO.LOW) #2
		GPIO.output(TWOS,GPIO.HIGH)
		print "TWO"
		time.sleep(DELAY)
		GPIO.output(ONES,GPIO.HIGH) #3
		GPIO.output(TWOS,GPIO.HIGH)
		print "THREE"
		time.sleep(DELAY)
		GPIO.output(ONES,GPIO.LOW) #4
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.HIGH)
		print "FOUR"
		time.sleep(DELAY)
		GPIO.output(ONES,GPIO.HIGH) #5
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.HIGH)
		print "FIVE"
		time.sleep(DELAY)
		GPIO.output(ONES,GPIO.LOW) #6
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.HIGH)
		print "SIX"
		time.sleep(DELAY)
		GPIO.output(ONES,GPIO.HIGH) #7
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.HIGH)
		print "SEVEN"
		time.sleep(DELAY)
		GPIO.output(ONES,GPIO.LOW) #8
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.HIGH)
		print "EIGHT"
		time.sleep(DELAY)
		GPIO.output(ONES,GPIO.HIGH) #9
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.HIGH)
		print "NINE"
		time.sleep(DELAY)
		GPIO.output(ONES,GPIO.LOW) #10
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.HIGH)
		print "TEN"
		time.sleep(DELAY)
		time.sleep(DELAY)

except KeyboardInterrupt:
	print "Aw common, let's count LED's forever."
	import os
	cmd = '/home/pi/bin/lo'
	os.system(cmd)
