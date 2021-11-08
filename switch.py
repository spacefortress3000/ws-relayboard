from gpiozero import *
import time

def switch(channel):
	if channel[2] == 'True':
		channel[0].on()
		print(channel[0], 'ON')
		time.sleep(channel[3]/1000)
		channel[0].off()
		print(channel[0], 'OFF')

	else:
		channel[0].toggle()
		print(channel[0], 'TOGGLE')