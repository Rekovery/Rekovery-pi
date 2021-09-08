from gpiozero import RGBLED
from gpiozero import Button
from gpiozero import DigitalInputDevice
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
onlineSlider = DigitalInputDevice(6)
button = Button(12)
button.wait_for_press()
button.when_pressed = changeVal
start = True

#start
    #0 = start
    #1 = stop


while True:
    
    if start:
        print("Rekovery LOG - Avvio modalita' Online"  if onlineSlider.value else "Rekovery LOG - Avvio modalita' Offline" )
        
        if(onlineSlider.value):
            statusLed.blink(0.2, 0.2, 0, 0, Color('blue'))
            while start:
                sleep(0.1)
            statusLed.color = Color("green")  
            sleep(2)
            statusLed.off()
        else:
                statusLed.blink(0.2, 0.2, 0, 0, Color('red'))
                time = datetime.now()

                if not os.path.isdir(PATH):
                    print("Rekovery LOG - Cartella non trovata, creazione...")
                    os.mkdir(PATH)
                print("Rekovery LOG - Avvio registrazione")

                #Chiudo e riavvio camera (riga 57) per efficienza energetica
                camera = picamera.PiCamera()
                camera.resolution = (1920, 1080)
                try:
                    camera.start_recording(f'{PATH}{time}.h264')

                    while start:
                        camera.wait_recording(0.1)
                except :
                    statusLed.blink(0.1, 0.1, 0, 0, Color('purple'))
                print("Rekovery LOG - Termino registrazione")
                camera.stop_recording()
                camera.close()
                
                #controllo correttezza registrazione

                statusLed.color = Color("green")  
                sleep(2)
                statusLed.off()
