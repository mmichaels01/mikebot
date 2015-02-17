import sys
import os
import time
import picamera
#Stream using MJPEG
#Streaming class for RPi Camera Module
#Written by Mike Michaels
class Stream:
	DEFAULT_PATH='/home/pi/img/stream.jpg'
	def __init__(self,frequency,duration,path=DEFAULT_PATH):
		self.frequency = frequency
		self.duration = duration
		self.path = path
	def SetPath(self,path):
		this.path=path
	def GetPath(self):
		return this.path
	def UpdateStreamImage(self):
		with picamera.PiCamera() as camera:
			camera.capture(self.path)	
	def StartStream(self):
		start=time.time()
		now=time.time()
		while(time.time() - start < self.duration):
			if(time.time() - now > self.frequency):
				self.UpdateStreamImage()
				now = time.time()
