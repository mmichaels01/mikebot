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
DELAY=1
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
		print "Going up..."
		print "ZERO"
		GPIO.output(ONES,GPIO.LOW) #0
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "ONE"
		GPIO.output(ONES,GPIO.HIGH) #1
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "TWO"
		GPIO.output(ONES,GPIO.LOW) #2
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "THREE"
		GPIO.output(ONES,GPIO.HIGH) #3
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "FOUR"
		GPIO.output(ONES,GPIO.LOW) #4
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "FIVE"
		GPIO.output(ONES,GPIO.HIGH) #5
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "SIX"
		GPIO.output(ONES,GPIO.LOW) #6
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "SEVEN"
		GPIO.output(ONES,GPIO.HIGH) #7
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "EIGHT"
		GPIO.output(ONES,GPIO.LOW) #8
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "NINE"
		GPIO.output(ONES,GPIO.HIGH) #9
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "TEN"
		GPIO.output(ONES,GPIO.LOW) #10
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "ELEVEN"
		GPIO.output(ONES,GPIO.HIGH) #11
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "TWELVE"
		GPIO.output(ONES,GPIO.LOW) #12
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "THIRTEEN"
		GPIO.output(ONES,GPIO.HIGH) #13
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "FOURTEEN"
		GPIO.output(ONES,GPIO.LOW) #14
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "FIFTEEN"
		GPIO.output(ONES,GPIO.HIGH) #15
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(3)
		print "Going down..."
		print "FOURTEEN"
		GPIO.output(ONES,GPIO.LOW) #14
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "THIRTEEN"
		GPIO.output(ONES,GPIO.HIGH) #13
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "TWELVE"
		GPIO.output(ONES,GPIO.LOW) #12
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "ELEVEN"
		GPIO.output(ONES,GPIO.HIGH) #11
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "TEN"
		GPIO.output(ONES,GPIO.LOW) #10
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "NINE"
		GPIO.output(ONES,GPIO.HIGH) #9
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "EIGHT"
		GPIO.output(ONES,GPIO.LOW) #8
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.HIGH)
		time.sleep(DELAY)
		print "SEVEN"
		GPIO.output(ONES,GPIO.HIGH) #7
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "SIX"
		GPIO.output(ONES,GPIO.LOW) #6
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "FIVE"
		GPIO.output(ONES,GPIO.HIGH) #5
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "FOUR"
		GPIO.output(ONES,GPIO.LOW) #4
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.HIGH)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "THREE"
		GPIO.output(ONES,GPIO.HIGH) #3
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "TWO"
		GPIO.output(ONES,GPIO.LOW) #2
		GPIO.output(TWOS,GPIO.HIGH)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		print "ONE"
		GPIO.output(ONES,GPIO.HIGH) #1
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.LOW)
		time.sleep(DELAY)
		GPIO.output(ONES,GPIO.LOW) #0
		GPIO.output(TWOS,GPIO.LOW)
		GPIO.output(FOURS,GPIO.LOW)
		GPIO.output(EIGHTS,GPIO.LOW)
		print "ZEROOOOO .... DUDE, LET'S COUNT UP AGAIN"
		time.sleep(3)

except KeyboardInterrupt:
	print "Oh, please don't stop this fun stuff!!!"
	import os
	cmd = '/home/pi/bin/lo'
	os.system(cmd)
