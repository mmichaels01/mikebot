from flask import Flask, render_template, request 
import RPi.GPIO as GPIO
import sys
import time
sys.path.append("/home/pi/pybin")
#print(str(sys.path))
import MikeBot
from MikeBot import DCWheel as Wheel
#from MikeBot.Ports import Ports
app = Flask(__name__)

@app.route("/")
def hello():
	templateData = {
	'WHAT' : 'OKAYYYYYYYYYY',
	}
	return render_template('template-master.html', **templateData)
	
@app.route("/get_input_left")
def get_input_left():
	GPIO.setmode(GPIO.BOARD)
	wheel = Wheel(12)
	wheel.TurnOn()
	time.sleep(1)
	wheel.TurnOff()
	return "Turn"
	

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)


