#Original from https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
# Modified 1.11.15 G. Oij
# this one suggests a voltage splitter using 1K and 2K resistors to
# split the 5v signal coming back from the HC-SR04 to 2/3 of 5V or ~3.3V 

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.cleanup()
import time
GPIO.setmode(GPIO.BOARD)

# Pin 18 for output
TRIG = 18
# Pin 22 for waiting for a reply after the speed of sound.
ECHO = 22
 
print "Distance Measurement In Progress"
 
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
 
GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(1)
 
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

pulse_start = 0
print"Before pulse_start" 
while GPIO.input(ECHO)==0:
	pulse_start = time.time()
 
print"pulse_start = ", pulse_start
while GPIO.input(ECHO)==1:
	pulse_end = time.time()
 
print"pulse_end = ", pulse_end

pulse_duration = pulse_end - pulse_start

# The distance that sound travels in a second is  343 Meters / Second
# So that is 34300 centimeters / second
# Since our sound pulse will be travelling round trip to the 
# CM to Inches conversion is * 0.393701

# I think this is wrong...  Should be doubled, not halved.
distance = pulse_duration * 17150
distanceininches = distance * 0.393701
 
distance = round(distance, 2)
distanceininches = round(distanceininches, 2) 
print "Distance:",distance,"cm"


print "Distance in inches: ",distanceininches
 
GPIO.cleanup()
