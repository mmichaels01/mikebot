import time
import os
import sys
from Stream import Stream

FREQUENCY = .2

if(len (sys.argv) > 1):
	time=int(sys.argv[1])
	if(len (sys.argv) > 2):
		path=sys.argv[2]	
		stream=Stream(FREQUENCY,time,path)
		stream.StartStream()
	else:
		stream=Stream(FREQUENCY,time)
		stream.StartStream()
