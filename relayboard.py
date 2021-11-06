import configparser
from gpiozero import *
import keyboard
import time

config = configparser.ConfigParser()
config.read('config.ini')

#Configurations from config.ini file
ch1_hotkey = str(config['ch1']['ch1_hotkey'])
ch1_timedelay = str(config['ch1']['ch1_timedelay'])
ch1_timedelaymillis = int(config['ch1']['ch1_timedelaymillis'])

ch2_hotkey = str(config['ch2']['ch2_hotkey'])
ch2_timedelay = str(config['ch2']['ch2_timedelay'])
ch2_timedelaymillis = int(config['ch2']['ch2_timedelaymillis'])

ch3_hotkey = str(config['ch3']['ch3_hotkey'])
ch3_timedelay = str(config['ch3']['ch3_timedelay'])
ch3_timedelaymillis = int(config['ch3']['ch3_timedelaymillis'])

ch4_hotkey = str(config['ch4']['ch4_hotkey'])
ch4_timedelay = str(config['ch4']['ch4_timedelay'])
ch4_timedelaymillis = int(config['ch4']['ch4_timedelaymillis'])

ch5_hotkey = str(config['ch5']['ch5_hotkey'])
ch5_timedelay = str(config['ch5']['ch5_timedelay'])
ch5_timedelaymillis = int(config['ch5']['ch5_timedelaymillis'])

ch6_hotkey = str(config['ch6']['ch6_hotkey'])
ch6_timedelay = str(config['ch6']['ch6_timedelay'])
ch6_timedelaymillis = int(config['ch6']['ch6_timedelaymillis'])

ch7_hotkey = str(config['ch7']['ch7_hotkey'])
ch7_timedelay = str(config['ch7']['ch7_timedelay'])
ch7_timedelaymillis = int(config['ch7']['ch7_timedelaymillis'])

ch8_hotkey = str(config['ch8']['ch8_hotkey'])
ch8_timedelay = str(config['ch8']['ch8_timedelay'])
ch8_timedelaymillis = int(config['ch8']['ch8_timedelaymillis'])

#Define GPIO
ch1 = 'ch1', ch1_hotkey, ch1_timedelay, ch1_timedelaymillis #OutputDevice(5)
ch2 = 'ch2', ch2_hotkey, ch2_timedelay, ch2_timedelaymillis #OutputDevice(6)
ch3 = 'ch3', ch3_hotkey, ch3_timedelay, ch3_timedelaymillis #OutputDevice(13)
ch4 = 'ch4', ch4_hotkey, ch4_timedelay, ch4_timedelaymillis #OutputDevice(16)
ch5 = 'ch5', ch5_hotkey, ch5_timedelay, ch5_timedelaymillis #OutputDevice(19)
ch6 = 'ch6', ch6_hotkey, ch6_timedelay, ch6_timedelaymillis #OutputDevice(20)
ch7 = 'ch7', ch7_hotkey, ch7_timedelay, ch7_timedelaymillis #OutputDevice(21)
ch8 = 'ch8', ch8_hotkey, ch8_timedelay, ch8_timedelaymillis #OutputDevice(26)

# Define hotkeys
keyboard.add_hotkey(ch1[1], lambda: switch(ch1))
keyboard.add_hotkey(ch2[1], lambda: switch(ch2))
keyboard.add_hotkey(ch3[1], lambda: switch(ch3))
keyboard.add_hotkey(ch4[1], lambda: switch(ch4))
keyboard.add_hotkey(ch5[1], lambda: switch(ch5))
keyboard.add_hotkey(ch6[1], lambda: switch(ch6))
keyboard.add_hotkey(ch7[1], lambda: switch(ch7))
keyboard.add_hotkey(ch8[1], lambda: switch(ch8))

def switch(channel):
	if channel[2] == 'True': #This needs to refer to config of the channel
		print(channel[0] + ' on') #channel.on()
		time.sleep(channel[3]/1000) #This needs to refer to config of the channel
		print(channel[0] + ' off') #channel.off()

	else:
		print(channel[0] + ' toggle') #channel.toggle()

keyboard.wait()