from Servo import Servo
import time
import os
import sys
from Ports import Ports
import RPi.GPIO as GPIO

try:
	if(len(sys.argv) >1):
		if(isinstance(int(sys.argv[1]),int)):
			deg=int(sys.argv[1])
			if(deg < 55):
				deg = 55
			elif(deg > 135):
				deg = 135
			servo=Servo(Ports.CAMERA_SERVO)
			servo.RotateTo(deg)
			servo.StopPWM()
finally:
	GPIO.cleanup()
