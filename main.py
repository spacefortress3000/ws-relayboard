from gpiozero import *
import keyboard
from switch import switch

#Configurations from config.ini file
ch1_hotkey = '1'
ch1_timedelay = False
ch1_timedelaymillis = 1000

ch2_hotkey = '2'
ch2_timedelay = False
ch2_timedelaymillis = 1000

ch3_hotkey = '3'
ch3_timedelay = False
ch3_timedelaymillis = 1000

ch4_hotkey = '4'
ch4_timedelay = False
ch4_timedelaymillis = 1000

ch5_hotkey = '5'
ch5_timedelay = False
ch5_timedelaymillis = 1000

ch6_hotkey = '6'
ch6_timedelay = False
ch6_timedelaymillis = 1000

ch7_hotkey = '7'
ch7_timedelay = False
ch7_timedelaymillis = 1000

ch8_hotkey = '8'
ch8_timedelay = False
ch8_timedelaymillis = 1000

#Define GPIO
ch1 = OutputDevice(5), ch1_hotkey, ch1_timedelay, ch1_timedelaymillis
ch2 = OutputDevice(6), ch2_hotkey, ch2_timedelay, ch2_timedelaymillis
ch3 = OutputDevice(13), ch3_hotkey, ch3_timedelay, ch3_timedelaymillis
ch4 = OutputDevice(16), ch4_hotkey, ch4_timedelay, ch4_timedelaymillis
ch5 = OutputDevice(19), ch5_hotkey, ch5_timedelay, ch5_timedelaymillis
ch6 = OutputDevice(20), ch6_hotkey, ch6_timedelay, ch6_timedelaymillis
ch7 = OutputDevice(21), ch7_hotkey, ch7_timedelay, ch7_timedelaymillis
ch8 = OutputDevice(26), ch8_hotkey, ch8_timedelay, ch8_timedelaymillis

# Define hotkeys
keyboard.add_hotkey(ch1[1], lambda: switch(ch1))
keyboard.add_hotkey(ch2[1], lambda: switch(ch2))
keyboard.add_hotkey(ch3[1], lambda: switch(ch3))
keyboard.add_hotkey(ch4[1], lambda: switch(ch4))
keyboard.add_hotkey(ch5[1], lambda: switch(ch5))
keyboard.add_hotkey(ch6[1], lambda: switch(ch6))
keyboard.add_hotkey(ch7[1], lambda: switch(ch7))
keyboard.add_hotkey(ch8[1], lambda: switch(ch8))

# Loop all channels off
channels = [ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8]
for channel in channels:
	channel[0].off()

def wait():
        keyboard.wait()

if __name__ == "__main__":
        wait()
