import sys
import os
from Sonar import Sonar
from Servo import Servo
from Ports import Ports
from DCWheel import DCWheel
import RPi.GPIO as GPIO
import time
import traceback

#Our board mode is board for all classes
GPIO.setmode(GPIO.BOARD)

debug = False
debug_time = 1


try:
    frontSonar = Sonar(Ports.FRONT_SONAR_TRIGGER, Ports.FRONT_SONAR_ECHO)
    leftSonar = Sonar(Ports.LEFT_SONAR_TRIGGER, Ports.LEFT_SONAR_ECHO)
    rightSonar = Sonar(Ports.RIGHT_SONAR_TRIGGER, Ports.RIGHT_SONAR_ECHO)
    frontSonarServo = Servo(Ports.FRONT_SONAR_SERVO)
    leftWheel = DCWheel(Ports.LEFT_DC_WHEEL)
    rightWheel = DCWheel(Ports.RIGHT_DC_WHEEL)


    #Slowly rotate from start to 150 deg
    frontSonarServo.RotateTo(150)
    frontSonarServo.RotateTo(30)
    frontSonarServo.RotateTo(90)
    #Turn off PWM so the servo stops twitching
    frontSonarServo.StopPWM()

    cameraServo = Servo(Ports.CAMERA_SERVO)
    cameraServo.RotateTo(60)
    cameraServo.RotateTo(120)
    cameraServo.RotateTo(90)
    cameraServo.StopPWM()

    print(frontSonar.GetDistanceInches())
    print(leftSonar.GetDistanceInches())
    print(rightSonar.GetDistanceInches())
    frontDistanceStart = frontSonar.GetDistanceInches()
    leftDistanceStart = leftSonar.GetDistanceInches()
    rightDistanceStart = rightSonar.GetDistanceInches()
    while True:
        frontDistance = frontSonar.GetDistanceInches()
        leftDistance = leftSonar.GetDistanceInches()
        rightDistance = rightSonar.GetDistanceInches()
        print ("Left-Start: " + str(leftDistanceStart))
        print ("Left: " + str(leftDistance))
        print ("Front-Start: " + str(frontDistanceStart))
        print ("Front: " + str(frontDistance))
        print ("Right-Start: " + str(rightDistanceStart))
        print ("Right: " + str(rightDistance))
        time.sleep(1)

#Message for our interrupts
except KeyboardInterrupt:
    print ("interrupted")
#Reference errors
except UnboundLocalError:
    print ("reference before initialization")
    traceback.print_exc(file=sys.stdout)
#Cleanup Tasks
finally:
    #frontSonarServo.pulse.stop()
    GPIO.cleanup()
