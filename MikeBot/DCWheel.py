import time
import os
import sys
import RPi.GPIO as GPIO

#Class designed for the control of Tower Pro 9g servo motors
#Written by Mike Michaels


class DCWheel(object):
    "Class for control of an individual DC Motor atached to a wheel"

    #Static Vars

    def __init__(self, gpio_port):
        self.gpio_port = gpio_port
        self.on = False
        GPIO.setup(self.gpio_port, GPIO.OUT)
        GPIO.output(self.gpio_port, False)

    def TurnOn(self):
        self.on = True
        GPIO.output(self.gpio_port, True)

    def TurnOff(self):
        self.off = False
        GPIO.output(self.gpio_port, False)

    def TurnOnTimed(self, timeSleep):
        self.on = True
        GPIO.output(self.gpio_port, True)
        time.sleep(timeSleep)
        GPIO.output(self.gpio_port, False)
        self.on = False

    def GetState(self):
        return self.on
        


