import thingspeak
import RPi.GPIO as GPIO
import time
channel_id =1506366
write_key="0XVJTIXHWLTMLYJX"

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 8
GPIO_ECHO = 10
GPIO.setwarnings(False)
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

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
		channel = thingspeak.Channel(id=channel_id,api_key=write_key)
		while True:
			dist = distance()
			print("Measured Distance = %.1f cm" % dist)
			channel.update({'field1': dist})
			time.sleep(15)
			
	except KeyboardInterrupt:
		print("Measuerment stopped by User")
		GPIO.cleanup()
