from gpiozero import RGBLED
from gpiozero import Button
from colorzero import Color
from time import sleep
from datetime import datetime
import picamera
import os

start = False

def changeVal(button):
    global start
    start = not start

PATH = os.path.expanduser('/home/pi/Videos/rekoveryOffline/')

statusLed = RGBLED(21, 20, 16)
modeOnline = False

button = Button(12)
button.wait_for_press()
button.when_pressed = changeVal

start = True

#start
    #0 = start
    #1 = stop

while start:
    
    if(modeOnline):
        statusLed.blink(0.2, 0.2, 0, 0, Color('blue'))

    else:
            statusLed.blink(0.2, 0.2, 0, 0, Color('red'))
            time = datetime.now()
            if not os.path.isdir(PATH):
                os.mkdir(PATH)
            camera = picamera.PiCamera()
            camera.resolution = (1920, 1080)
            camera.start_recording(f'{PATH}{time}.h264')

            while start:
                #print (start)
                sleep(0.1)
            
            camera.stop_recording()
    
