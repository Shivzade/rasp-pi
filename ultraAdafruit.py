#pip3 install adafruit-io

import time
import RPi.GPIO as GPIO
from Adafruit_IO import Client

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO_TRIGGER = 8
GPIO_ECHO = 10

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

ADAFRUIT_IO_USERNAME = "Shiv_Zade"
ADAFRUIT_IO_KEY = "aio_cxkI41HstxvVuKSjeqvnJLtK8yld"

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

distance_feed = aio.feeds('distance')

def distance ():
	# set Trigger to HIGH
	GPIO.output(GPIO_TRIGGER, True)
	
	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	StartTime = time.time()
	StopTime = time.time()
	# save StartTime
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
	# save time of arrival
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
		
	TimeElapsed = StopTime - StartTime
	distance =  (TimeElapsed * 34300) / 2
	
	return distance
	

	
while True:
    dist = distance() 
    print ("Measured Distance = %.1f cm" % dist)
    try:
        aio.send(distance_feed.key, str(dist))
        time.sleep(5)
    except:
        print("Exception occured..")
