import time
import os
import sys
import RPi.GPIO as GPIO
from DCWheel import DCWheel
from Ports import Ports
from threading import Thread

GPIO.setmode(GPIO.BOARD)

#Class designed for DC Motor Control
#Written by Mike Michaels 3/2/15
threads = []
try:
    for i in range(0,5):
        leftWheel = DCWheel(Ports.LEFT_WHEEL)
        rightWheel = DCWheel(Ports.RIGHT_WHEEL)
        threads.append(Thread(target = leftWheel.TurnOnTimedRatio, args = (.1,1,)))
        leftId = len(threads) - 1
        threads[leftId].name = "left"
        rightThread = Thread(target = rightWheel.TurnOnTimedRatio, args = (.1,1,))
        threads[leftId].start()
        rightThread.start()
        threads[leftId].join()
        del threads[leftId]
        rightThread.join()
        print(threads)
        print("done")

finally:
    GPIO.cleanup()


