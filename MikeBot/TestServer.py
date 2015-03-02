import os
import sys
import time
from socket import socket
from ServerSocket import ServerSocket
from DCWheel import DCWheel
from Ports import Ports
import RPi.GPIO as GPIO
from threading import Thread

GPIO.setmode(GPIO.BOARD)

leftWheelValue = 0
rightWheelValue = 0
leftWheel = DCWheel(Ports.LEFT_WHEEL)
rightWheel = DCWheel(Ports.RIGHT_WHEEL)
threads = {'Left' : Thread() , 'Right' : Thread()}

def parseWheel(str):

    arr = str.split(',')
    leftWheelValue = float(arr[1])
    rightWheelValue = float(arr[2])
##    print (str)
##    print(leftWheelValue)
##    print(rightWheelValue)
##    if(threads['Left'] is None or not threads['Left'].is_running()):
##        threads['Left'] = Thread(target = leftWheel.TurnOnTimedRatio, args = (leftWheelValue,.5,))
##        threads['Left'].start()
##    if(threads['Right'] is None or not threads['Right'].is_running()):
##        threads['Right'] = Thread(target = rightWheel.TurnOnTimedRatio, args = (rightWheelValue,.5,))
##        threads['Right'].start()
    if(not threads['Left'].is_alive() and leftWheelValue > .1):
        threads['Left'] = Thread(target = leftWheel.TurnOnTimedRatio, args = (leftWheelValue,.2,))
        threads['Left'].start()
    if(not threads['Right'].is_alive() and rightWheelValue > .1):
        threads['Right'] = Thread(target = rightWheel.TurnOnTimedRatio, args = (rightWheelValue,.2,))
        threads['Right'].start()
    print(threads)
    return

def parseCamera(str):
    print (str)
    return

try:
    sock = ServerSocket()
    for i in sock.readUDP():
        #print(time.time())
        if i.find('bot') != -1:
            print('bot started')
        if i.find('wheels') != -1:
            parseWheel(i)
        if i.find('camera') != -1:
            parseCamera(i)
        
        
finally:
    print('done')
