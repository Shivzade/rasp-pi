import thingspeak
import RPi.GPIO as GPIO
import time
channel_id =1505494
write_key="0R0J51II60TVC2HS"

ir =8


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(ir, GPIO.IN)

if __name__ == "__main__":
	count = 0
	channel = thingspeak.Channel(id=channel_id,api_key=write_key)
	while True:
		sensorValue = GPIO.input(ir)
		print(sensorValue)
		if sensorValue:
			print("Nobody is passing by..")
			count = count
		else:
			print("counter increased")
			count += 1
	
	print(count)
	channel.update({'field1': count, 'field2': count})
	
	time.sleep(1)
	

