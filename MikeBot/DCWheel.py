import time
import os
import sys
import RPi.GPIO as GPIO

#Class designed for DC Motor Control
#Written by Mike Michaels 3/2/15

class DCWheel(object):
    "Class for control of an individual DC Motor atached to a wheel"

    #Static Vars

    def __init__(self, gpio_port):
        self.gpio_port = gpio_port
        self.on = False
        self.ratio = 0.00
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

   # def TurnToRatio(self, ratio):
   #     while(self.ratio != ratio):
   #         print(ratio)
   #         diff = (ratio - self.ratio) / float(10)
   #         self.ratio += diff
   #         time.sleep(.1)
   #         yield self.ratio
            
    def TurnOnTimedRatio(self, ratio, duration):
        start = time.time()
        while((time.time() - start) < duration):
            #print("on")
            GPIO.output(self.gpio_port, True)
            time.sleep(float(ratio) / 500.0)
            GPIO.output(self.gpio_port, False)
            time.sleep(.0005)
        return
    
    def GetState(self):
        return self.on
        


