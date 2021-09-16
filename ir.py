import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
i = 0

while 1:
	
	if (GPIO.input(14)) ==0:
		i += 1
		
		print(i)
	sleep(1)



	
	
	
