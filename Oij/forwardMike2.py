import time
# Import the Raspberry Pi GPIO libraries that
# allow us to connect the Raspberry Pi to
# other physical devices via the General
# Purpose Input-Output (GPIO) pins
import RPi.GPIO as GPIO
import os



###
###CONSTANTS
###

#1==RIGHT, 2==FORWARD, 3==LEFT

# Pin 24 for output
TRIG3 = 24
# Pin 26 for waiting for a reply after the speed of sound.
ECHO3 = 26
# Pin 18 for output
TRIG1 = 18
# Pin 22 for waiting for a reply after the speed of sound.
ECHO1 = 22
#Pin 16 for right wheel
RIGHTWHEEL=16
#Pin 12 for left wheel
LEFTWHEEL=12
# Pin 21 for output
TRIG2 = 21
# Pin 19 for waiting for a reply after the speed of sound.
ECHO2 = 19


TIME_ON_LEFT  = .02
TIME_ON_RIGHT = .02
MOVE_TIME_PER_SCAN = .5
DELAY = 0.01

DEBUG = False

###
###VARS
###
#GPIO SETTING
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
GPIO.setup(RIGHTWHEEL,GPIO.OUT)
GPIO.setup(LEFTWHEEL,GPIO.OUT)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)

GPIO.output(RIGHTWHEEL,GPIO.LOW)
GPIO.output(LEFTWHEEL,GPIO.LOW)

#Set these ahead of time so we don't potentially get null reference errors
pulse_start1 = time.time()
pulse_end1 = pulse_start1 + 0.5

###METHODS
def Reading(Trig,Echo):
        GPIO.output(Trig, False)   
        #print "Waiting For Ultrasonic Sensor To Settle"
        #time.sleep(0.5)
 
        GPIO.output(Trig, True)
        time.sleep(0.00001)
        GPIO.output(Trig, False)

        pulse_start1 = 0
        #print"Before pulse_start1" 
        while GPIO.input(Echo)==0:
            pulse_start1 = time.time()
 
        #print"pulse_start1 = ", pulse_start1
        while GPIO.input(Echo)==1:
            pulse_end1 = time.time()
 
        #print"pulse_end1 =   ", pulse_end1

        pulse_duration = pulse_end1 - pulse_start1
        #print "pulse_duration = ", pulse_duration

        # The distance that sound travels in a second is  343 Meters / Second
        # So that is 34300 centimeters / second
        # Since our sound pulse will be travelling round trip to the 
        # divide that by two
        # CM to Inches conversion is * 0.393701

        distance = pulse_duration * 17150
        distanceininches = distance * 0.393701
 
        distance = round(distance, 2)
        distanceininches = round(distanceininches, 2) 
        #print "Distance:",distance,"cm"

        #print "Distance in inches: ",distanceininches
        #print "Distance in feet: ",distanceininches / 12
                #time.sleep(DELAY)
                #GPIO.output(RIGHTWHEEL,GPIO.HIGH)
                #GPIO.output(LEFTWHEEL,GPIO.HIGH)
                #time.sleep(DELAY)
                #GPIO.output(RIGHTWHEEL,GPIO.LOW)
                #GPIO.output(LEFTWHEEL,GPIO.LOW)
        return distanceininches

def MoveBot(moveTime, timeOnRight, timeOnLeft):
        start_time = time.time()
        while(time.time() - start_time < moveTime):
            GPIO.output(RIGHTWHEEL, GPIO.HIGH)
            time.sleep(timeOnRight)
            GPIO.output(RIGHTWHEEL, GPIO.LOW)
            #time.sleep(DELAY)
            GPIO.output(LEFTWHEEL, GPIO.HIGH)
            time.sleep(timeOnLeft)
            GPIO.output(LEFTWHEEL, GPIO.LOW)
            #time.sleep(DELAY)

        return

def FullBlast(moveTime):
        start_time = time.time()
        while(time.time() - start_time < moveTime):
            GPIO.output(RIGHTWHEEL, GPIO.HIGH)
            GPIO.output(LEFTWHEEL, GPIO.HIGH)
        GPIO.output(LEFTWHEEL, GPIO.LOW)
        GPIO.output(RIGHTWHEEL, GPIO.LOW)
        return

def MoveBot2(moveTime, timeOnRight, timeOnLeft):
        start_time = time.time()
        while(time.time() - start_time < moveTime):
            GPIO.output(RIGHTWHEEL, GPIO.HIGH)
            time.sleep(timeOnRight)
            GPIO.output(RIGHTWHEEL, GPIO.LOW)
            time.sleep(DELAY)
            GPIO.output(LEFTWHEEL, GPIO.HIGH)
            time.sleep(timeOnLeft)
            GPIO.output(LEFTWHEEL, GPIO.LOW)
            time.sleep(DELAY)

        return

try:
    cmd = 'mpg123 /home/pi/sounds/Be*.mp3 > /dev/null 2>/dev/null &'
    LEFT_INITIAL = Reading(TRIG3, ECHO3)
    RIGHT_INITIAL = Reading(TRIG1, ECHO1)
    FORWARD_INITIAL = Reading(TRIG2, ECHO2)
    leftDistanceInches = LEFT_INITIAL
    rightDistanceInches = RIGHT_INITIAL
    forwardDistanceInches = FORWARD_INITIAL
    while True:
        lastLeft = leftDistanceInches
      # lastRight = rightDistanceInches
        lastForward = forwardDistanceInches
        leftDistanceInches = Reading(TRIG3, ECHO3)
      # rightDistanceInches = Reading(TRIG1, ECHO1)
        forwardDistanceInches = Reading(TRIG2, ECHO2)
        
        if(forwardDistanceInches < 1 or leftDistanceInches < 1 or rightDistanceInches < 1):
            print "Object too close in front, stopping"
            break
        if(abs(LEFT_INITIAL - leftDistanceInches) > 2):
            if(FORWARD_INITIAL - forwardDistanceInches > 2):
                #Turning left
                TIME_ON_LEFT = .03
            if(FORWARD_INITIAL - forwardDistanceInches < -2):
                #Turning right
                TIME_ON_RIGHT = .03
        
        MoveBot(MOVE_TIME_PER_SCAN,TIME_ON_RIGHT,TIME_ON_LEFT)
        #FullBlast(5)


        TIME_ON_LEFT = .02
        TIME_ON_RIGHT = .02

        print "WHEEL SPIN TIME LEFT: ", TIME_ON_LEFT
        print "WHEEL SPIN TIME RIGHT: ", TIME_ON_RIGHT
        print "DISTANCE LEFT: ", leftDistanceInches
        print "DISTANCE RIGHT: ", rightDistanceInches
        print "DISTANCE FORWARD: ", forwardDistanceInches
        #Slow it down to debug some crap
        if(DEBUG):
            time.sleep(3)


except KeyboardInterrupt:
	print "Interrupted"
	GPIO.output(RIGHTWHEEL,GPIO.LOW)
	GPIO.output(LEFTWHEEL,GPIO.LOW)

