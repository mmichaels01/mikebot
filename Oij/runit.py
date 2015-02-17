#import the GPIO library to access the pins
#1Jeopardy1.wav  2POPPYCOK.WAV  3Hawks1.wav  RODENT.WAV
import os
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
#use the BCM pin numbers
GPIO.cleanup()
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

#set variables for corresponding LED outputs
BLUE=11
GREEN=13
RED=15

GPIO.setup(BLUE,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)

#Turn them off if they are on
GPIO.output(BLUE,GPIO.LOW)
GPIO.output(GREEN,GPIO.LOW)
GPIO.output(RED,GPIO.LOW)

#set switch pins as inputs
SWITCH1=22
SWITCH2=24
SWITCH3=26
GPIO.setup(SWITCH1, GPIO.IN)
GPIO.setup(SWITCH2, GPIO.IN)
GPIO.setup(SWITCH3, GPIO.IN)


DELAY=.05


try:
	#start a forever loop
	while True:
		#check if the switch has been pressed
		if(GPIO.input(SWITCH1) == 0):
			#Turn on the BLUE LED.
			#print ("Hey, the BLUE LED should be high!")
			GPIO.output(BLUE, GPIO.HIGH) 
			cmd = 'cd /home/pi/sounds/; sudo aplay 1Jeopardy1.wav > /dev/null'
			os.system(cmd)
			#print ("Input on %d is 0" % SWITCH1)
			
		else:	#Not pressed, then set pin to a LOW output
			GPIO.output(BLUE, GPIO.LOW)
			#print ("Input on %d is 1" % SWITCH1)

		if(GPIO.input(SWITCH2) == 0):
			GPIO.output(GREEN, GPIO.HIGH) 
			#cmd = 'cd /home/pi/sounds/; sudo aplay 2POPPYCOK.WAV 2 > /dev/null'
			cmd = 'cd /home/pi/sounds/; sudo aplay RODENT.WAV > /dev/null'
			os.system(cmd)
			#print ("Input on %d is 0" % SWITCH2)
			
		else:	#Not pressed, then set pin to a LOW output
			GPIO.output(GREEN, GPIO.LOW)
			#print ("Input on %d is 1" % SWITCH2)

		if(GPIO.input(SWITCH3) == 0):
			#Turn on the RED LED.
			#print ("Hey, the RED LED should be high!")
			GPIO.output(RED, GPIO.HIGH) 
			cmd = 'cd /home/pi/sounds/; sudo aplay 3Hawks1.wav > /dev/null'
			os.system(cmd)
			#print ("Input on %d is 0" % SWITCH3)
			
		else:	#Not pressed, then set pin to a LOW output
			GPIO.output(RED, GPIO.LOW)
			#print ("Input on %d is 1" % SWITCH3)

		time.sleep(DELAY)

except KeyboardInterrupt:
	print "Hit interrupt."
	cmd = '/home/pi/bin/lo'
	os.system(cmd)
