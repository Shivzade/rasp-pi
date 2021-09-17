#pip3 install adafruit-io

import time
import RPi.GPIO as GPIO
from Adafruit_IO import Client

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)

ADAFRUIT_IO_USERNAME = "Shiv_Zade"
ADAFRUIT_IO_KEY = "aio_MdQo67sDwbKvOAULjyyLs9OSJqSz"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
Light_feed = aio.feeds('light')

while True:
    print("Receiving data..")
    status = aio.receive(Light_feed.key).value
    print(status)
    if status == "ON":
        GPIO.output(8,True)
        print("LED ON")
    else:
        GPIO.output(8,False)
        print("LED OFF")
        time.sleep(5)
        
        
       
      
