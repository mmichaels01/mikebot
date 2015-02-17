import time
import os
import sys
from Stream import Stream

if(len sys.argv > 0):
	time=int(sys.argv[1])
	if(len sys.argv > 1):
		path=sys.argv[2]	
		stream=Stream(
