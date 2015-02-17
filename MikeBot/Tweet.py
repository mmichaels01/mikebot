import sys
import time
import picamera
from twython import Twython
from TwitterKeys import TwitterKeys

#Automated twitter script for bot
#Written by Mike Michaels

twitter=Twython(TwitterKeys.CONSUMER_KEY,TwitterKeys.CONSUMER_SECRET,TwitterKeys.ACCESS_KEY, TwitterKeys.ACCESS_SECRET)

if(len(sys.argv) == 3 and sys.argv[2] == 'pic'):
	timestr=str(int(time.time()))
	path='/home/pi/img/'+timestr+'.jpg'
	with picamera.PiCamera() as camera:
		camera.capture(path)
	photo=open(path, 'rb')
	media_upload=twitter.upload_media(media=photo)
	twitter.update_status(media_ids=[media_upload['media_id']],status=sys.argv[1])
	photo.close()
elif(len(sys.argv) == 2):
	twitter.update_status(status=sys.argv[1])
else:
	print("Incorrect usage - [script] [status] [pic=false]")
	print(str(len(sys.argv)))
	print(sys.argv)
