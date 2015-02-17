#!/usr/bin/python
# G. Oij Modified aim.py to goose the horizontal servo motor
# First converts degrees to pulse width
import sys
if len (sys.argv) != 2 :
    print "Usage: python aim.py DEGREES_TO_AIM"
    sys.exit (1)

DEGREES = float(sys.argv[1])

# This formula converts the number of degrees (0 - 180) that these
# servo motors can rotate to a pulse width that will move the
# aiming servo appropriately.

# 2.5% of 20ms is .5ms or 500 microseconds.  This pulse width will
# move the servo motor to 0 degrees.

# 7.5% of 20ms is 1.5ms.  This pulse width will move the servo to 90 degrees.

# 12.5% of 20ms is 2.5ms.  This pulse width will move the servo to 180 degrees.

PULSEWIDTH = ((DEGREES/18) + 2.5)
print DEGREES
print " was converted to pulse width of %.2f milliseconds." % (20 * PULSEWIDTH / 100)


import RPi.GPIO as GPIO
import time
#
# The towerpro servo motor moves based on duration of pulses sent to it.
# This illustration shows how to rotate the motor at 90 degree increments.


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

#Use Pin 10 as output to control the horizontal servo motor
SERVOPIN=10
GPIO.setup(SERVOPIN,GPIO.OUT)

LED=23
#Flash the light
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,GPIO.HIGH)
time.sleep(.1)
GPIO.output(LED,GPIO.LOW)
time.sleep(.1)
GPIO.output(LED,GPIO.HIGH)
time.sleep(.1)
GPIO.output(LED,GPIO.LOW)
p = GPIO.PWM(SERVOPIN,50)

# Use 2.5% of 20ms as zero degrees
# Use 12.5% of 20ms as 180 degrees
START=2.5
DELAY=.5
p.start(START)

#time.sleep(DELAY)
p.ChangeDutyCycle(PULSEWIDTH)
time.sleep(DELAY)
GPIO.cleanup()
