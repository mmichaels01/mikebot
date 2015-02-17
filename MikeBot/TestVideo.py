import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.start_recording('/home/pi/vid/1.h264')
    camera.wait_recording(5)
    camera.stop_recording()
