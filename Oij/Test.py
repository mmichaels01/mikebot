import sys
import os
from Sonar import Sonar
import RPi.GPIO as GPIO
import time
try:
    frontSonar = Sonar(24,26)
    print("Inches: " + str(frontSonar.GetDistanceInches()))
except KeyboardInterrupt:
    GPIO.cleanup()