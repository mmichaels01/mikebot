#Original from https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
# Modified 1.11.15 G. Oij
# this one suggests a voltage splitter using 1K and 2K resistors to
# split the 5v signal coming back from the HC-SR04 to 2/3 of 5V or ~3.3V 

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.cleanup()
import time
#Use the pin numbers on the GPIO to address the pins
GPIO.setmode(GPIO.BOARD)

# Pin 18 for output
TRIG1 = 18
# Pin 22 for waiting for a reply after the speed of sound.
ECHO1 = 22
 
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
 
GPIO.output(TRIG1, False)
print "Waiting For Ultrasonic Sensor To Settle"
time.sleep(2)
 
GPIO.output(TRIG1, True)
time.sleep(0.00001)
#time.sleep(0.00001) # Original
GPIO.output(TRIG1, False)

pulse_start1 = 0
#print"Before pulse_start1" 
while GPIO.input(ECHO1)==0:
	pulse_start1 = time.time()
 
#print"pulse_start1 = ", pulse_start1
while GPIO.input(ECHO1)==1:
	pulse_end1 = time.time()
 
#print"pulse_end1 =   ", pulse_end1

pulse_duration = pulse_end1 - pulse_start1
print "pulse_duration = ", pulse_duration

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
print "Distance in inches: ", distanceininches

GPIO.cleanup()
