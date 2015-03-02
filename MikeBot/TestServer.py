import os
import sys
import time
from socket import socket
from ServerSocket import ServerSocket
from DCWheel import DCWheel
from Ports import Ports
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

leftWheelValue = 0
rightWheelValue = 0
leftWheel = DCWheel(Ports.LEFT_WHEEL)
rightWheel = DCWheel(Ports.RIGHT_WHEEL)

def parseWheel(str):
    print (str)
    arr = str.split(',')
    leftWheelValue = float(arr[1])
    rightWheelValue = float(arr[2])

    print(leftWheelValue)
    print(rightWheelValue)
    
    if (leftWheelValue > .1):
        print("left on")
        leftWheel.TurnOn()
    elif (leftWheelValue <= .1) :
        print("left off")
        leftWheel.TurnOff()

    if (rightWheelValue > .1):
        print("right on")
        rightWheel.TurnOn()
    elif (rightWheelValue <= .1):
        print("right off")
        rightWheel.TurnOff()
        
    return

def parseCamera(str):
    print (str)
    return

try:
    sock = ServerSocket()
    for i in sock.readUDP():
        print(time.time())
        if i.find('bot') != -1:
            print('bot started')
        if i.find('wheels') != -1:
            parseWheel(i)
        if i.find('camera') != -1:
            parseCamera(i)
        
        
finally:
    print('done')
