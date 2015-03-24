import time
import os
import sys
import RPi.GPIO as GPIO

#Class designed for the control of Tower Pro 9g servo motors
#Written by Mike Michaels

class Servo:
    #Class String
    'Class for the Tower Pro 9g Servos'

    #Constructor for our servo 9g
    def __init__(self, gpio_port):
        self.gpio_port = gpio_port
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.gpio_port, GPIO.OUT)

        #Set the PWM on the port
        self.pulse = GPIO.PWM(self.gpio_port, 50)

        #7.5% is neutral position of servo
        self.pulse_width = 7.5
        self.pulse.start(self.pulse_width)

        #Start at 90 degrees
        self.angle = 90
        self.rotationFrequency = .01
        self.rotationDegrees = .1

	self.RotateTo(self.angle)


    def GetAngle(self, angle):
        return self.angle

    def GetPulseWidth(self, degree):
        return (2.5 + (10.0 / 180.0) * degree)

    def SetPulseWidth(self, pulseWidth):
        self.pulse_width = pulseWidth
        self.pulse.ChangeDutyCycle(self.pulse_width)
    
    def RotateTo(self, degree):
        if(degree > 180):
            degree = 180
        elif(degree < 0):
            degree = 0
        newDuty = self.GetPulseWidth(degree)
        while(round(self.pulse_width, 1) != round(newDuty,1)):
            if(newDuty > self.pulse_width):
                self.pulse_width += self.rotationDegrees
                self.SetPulseWidth(self.pulse_width)
            else:
                self.pulse_width -= self.rotationDegrees
                self.SetPulseWidth(self.pulse_width)            
            time.sleep(self.rotationFrequency)
        self.angle = degree
    
    #2.5 pulse-width modulation for 0 degrees
    #12.5 pulse-wdith mulation for 180 degrees
    def SnapTo(self, degree):
        if (degree > 180):
            degree = 180
        elif ( degree < 0):
            degree = 0
        self.pulse_width = self.GetPulseWidth(degree)
        self.pulse.ChangeDutyCycle(self.pulse_width)
        self.angle = 1
        time.sleep(1)

    def StopPWM(self):
        self.pulse.stop()
