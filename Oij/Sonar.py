import time
import sys
import RPi.GPIO as GPIO
import os

class Sonar:
    #Class string
    'Class for the HC-SR04 Sonar Sensors'

    #Static variables


    #Constructor
    def __init__(self, gpio_trigger_port, gpio_echo_port):
        #Set the port values
        self.gpio_trigger_port = gpio_trigger_port
        self.gpio_echo_port = gpio_echo_port 

    def Sense(self):
        #GPIO settings
        GPIO.setmode(GPIO.BOARD)

        #Setup the port to sense
        GPIO.setup(self.gpio_trigger_port, GPIO.OUT)
        GPIO.setup(self.gpio_echo_port, GPIO.IN)
        
        GPIO.output(self.gpio_trigger_port, True)
        time.sleep(0.000005)
        GPIO.output(self.gpio_trigger_port, False)

        startTime = 0
        endTime = .1

        GPIO.output(self.gpio_trigger_port, True)
        time.sleep(0.00)
        GPIO.output(self.gpio_trigger_port, False)

        #while GPIO.input(self.gpio_echo_port) == 1:
        #    print ("WHY IS THIS HIGH")
        while GPIO.input(self.gpio_echo_port) == 0:
            startTime=time.time()
            print ("WE LOW")
            #time.sleep(1)
        while GPIO.input(self.gpio_echo_port) == 1:
            endTime=time.time()
            print ("WE HIGH")
            continue
        endTime = time.time()

        pulse_duration = endTime - startTime
        print(str(pulse_duration))
        GPIO.cleanup()

        print(str(time.time()))
        return pulse_duration

    #Speed of sound is approximately 343 meters per second
    #the value we are calculating is the time in seconds from when the trigger
    #was fired
    #to when our echo is received.  We halve this to account for both
    #directions
    #distanceMultiplierMeters = 171.5
    #distanceMultiplierCentimeters = 17150
    #distanceMultiplierFeet = 562.664
    #distanceMultiplierInches = 6751.97


    def GetDistanceMeters(self):
        return (round(self.Sense() * 171.5,3))

    def GetDistanceCentimeters(self):
        return (round(self.Sense() * 17150,3))
    
    def GetDistanceFeet(self):
        return (round(self.Sense() * 562.664,3))

    def GetDistanceInches(self):
        return (round(self.Sense() * 6751.97,3))

    def TestMeth(self):
        return