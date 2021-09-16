import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 8
GPIO_ECHO = 10
GPIO_LED = 12
GPIO.setwarnings(False)
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_LED, GPIO.OUT)
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
	
if __name__ == '__main__':
	try:
		while True:
			dist = distance()
			print("Measured Distance = %.if cm" % dist)
			time.sleep(0.1)
		
			if dist<10:
				print("Danger")
				GPIO.output(GPIO_LED, True)
			else:
				print("Safe")
				GPIO.output(GPIO_LED, False)			
	except KeyboardInterrupt:
		print("Measyerment stopped by User")
		GPIO.cleanup()
