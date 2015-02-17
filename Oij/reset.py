#!/usr/bin/python
# G. Oij 6/2/14
# First converts degrees to pulse width
import sys
if len (sys.argv) != 1 :
    print "Usage: python aim.py NO ARGS, MAN!"
    sys.exit (1)

DEGREES = 1.5

# This formula converts the number of degrees (0 - 180) that these
# servo motors can rotate to a pulse width that will move the
# aiming servo appropriately.

# 2.5% of 20ms is .5ms or 500 microseconds.  This pulse width will
# move the servo motor to 0 degrees.

# 7.5% of 20ms is 1.5ms.  This pulse width will move the servo to 90 degrees.

# 12.5% of 20ms is 2.5ms.  This pulse width will move the servo to 180 degrees.

PULSEWIDTH = (1.5)
print DEGREES
print " was converted to pulse width of %.2f milliseconds." % (20 * PULSEWIDTH / 100)


import RPi.GPIO as GPIO
import time
#
# The towerpro servo motor moves based on duration of pulses sent to it.
# This illustration shows how to rotate the motor at 90 degree increments.


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

#Use Pin 13 as output to control the aiming servo motor
SERVOPIN=13
GPIO.setup(SERVOPIN,GPIO.OUT)

p = GPIO.PWM(SERVOPIN,50)

# Use 2.5% of 20ms as zero degrees
# Use 12.5% of 20ms as 180 degrees
START=2.5
DELAY=.5
p.start(START)

p.ChangeDutyCycle(7.5)
time.sleep(DELAY)
