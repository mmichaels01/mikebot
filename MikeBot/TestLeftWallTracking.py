import sys
import os
import RPi.GPIO as GPIO
import time
import traceback
from Sonar import Sonar
from Servo import Servo
from Ports import Ports
from DCWheel import DCWheel


#Our board mode is board for all classes
GPIO.setmode(GPIO.BOARD)

debug = False
debug_time = 1


try:
    frontSonar = Sonar(Ports.FRONT_SONAR_TRIGGER, Ports.FRONT_SONAR_ECHO)
    leftSonar = Sonar(Ports.LEFT_SONAR_TRIGGER, Ports.LEFT_SONAR_ECHO)
    rightSonar = Sonar(Ports.RIGHT_SONAR_TRIGGER, Ports.RIGHT_SONAR_ECHO)
    frontSonarServo = Servo(Ports.FRONT_SONAR_SERVO)
    leftWheel = DCWheel(Ports.LEFT_WHEEL)
    rightWheel = DCWheel(Ports.RIGHT_WHEEL)
    #Slowly rotate from start to 150 deg
    frontSonarServo.RotateTo(180)
    #Turn off PWM so the servo stops twitching
    frontSonarServo.StopPWM()

    frontDistanceStart = frontSonar.GetDistanceInches()
    leftDistanceStart = leftSonar.GetDistanceInches()
    rightDistanceStart = rightSonar.GetDistanceInches()



    time.sleep(.5)
    while True:
        leftWheelOnTime = 0.02
        rightWheelOnTime = 0.02
        frontDistance = frontSonar.GetDistanceInches()
        leftDistance = leftSonar.GetDistanceInches()
        rightDistance = rightSonar.GetDistanceInches()
        print ("Left-Start: " + str(leftDistanceStart))
        print ("Left: " + str(leftDistance))
        print ("Front-Start: " + str(frontDistanceStart))
        print ("Front: " + str(frontDistance))
        print ("Right-Start: " + str(frontDistanceStart))
        print ("Right: " + str(frontDistance))

        if(leftDistance < 2 or frontDistance < 2 or rightDistance < 2):
            print("Object too close")
            print("LeftDist="+str(leftDistance))
            print("FrontDist="+str(frontDistance))
            print("RightDist="+str(rightDistance))
            #break
       
        now = time.time()
        #Left wall is getting further
        #Are we turning inward or outward
        while(time.time() - now < .1):
            if(abs(leftDistance - leftDistanceStart) > 2):
                #If the front distance on front is getting bigger, we are turning outward
                if(frontDistance - frontDistanceStart > 2):
                    rightWheelOnTime = 0.03
                #The distance on front is getting smaller; we are turning inward
                elif(frontDistance - frontDistanceStart < 2):
                    leftWheelOnTime = 0.03

            leftWheel.TurnOnTimed(leftWheelOnTime)
            rightWheel.TurnOnTimed(rightWheelOnTime)

        if(debug):
            time.sleep(debug_time)

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
