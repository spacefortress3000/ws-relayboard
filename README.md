# Hey feller! :cowboy_hat_face: This is spacecowboy3000, I'm thrilled you found my repository!

1. This tool is for controlling Raspberry Pi's GPIO's and a WaveShare 8 channel relay board attached to it. The Pi's purpose in this tool is only to control 8 channel relay board. This tool will allow you to control all 8 channel from the Pi itself with keyboard, from command line (and SSH), and from another computer. Sections 2, 3 and 4 will cover these ways of controlling the relay board.
+ Libraries used can be found from requirements.txt. If you do not have the libraries you may install them by typing `pip install` and the `name_of_the_library`.
+ The relay board used in this tool is https://www.waveshare.com/wiki/RPi_Relay_Board_(B). Manual can be found from the depository folder. The code in this repository may not apply to other relay boards since GPIO's used in this tool may not be the same in every board. Best way to find the correct wiring is to look from the board's manual.
+ GPIO's used are 5, 6, 13, 16, 19, 20, 21, and 26 (BCM). Channel numbering go from right to left. For example GPIO 5 controlls channel 1 and GPIO 6 controls channel 2 etc. Please note that all GPIO pin numbers gpiozero library use are Broadcom (BCM) numbering by default. In order to change pin numbering found here: https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering.
+ Configuration are stated in main.py file. You may change the hotkeys, time delay on/off and time delay itself in milliseconds.
  + Hotkeys are by default set to 1,2,3,4... to control channels. Each number pressed refers to the same number of channel. Changing the hotkeys is done in main.py file. Please note that use only text format. For example ctrl+1
  + Time delay on/off set value in main.py either True if you want delayed on/off or False. Delayed on/off sets the channel on and after certain number of milliseconds turns the channel off.
  + Time delay Set the delay in milliseconds meaning 1 second is 1000 milliseconds. You do the math.

2. In order to control the GPIO's from the Pi itself you need to attach a keyboard or numbad to it.
+ Controlling GPIO's are done by hotkeys which are by default set to 1,2,3,...8 Numbers typed refers to channel numbers. For example pressing '1' will do the task for channel 1. You may use your own hotkey for every channel. Hotkey can be changed in main.py file e.g. type in terminal `sudo nano /home/pi/ws-relayboard/main.py`. See format specifics from previous section.

3. Running commands from command Raspberry Pi's command line or when SSH'ing to Pi (This is an example and I would prefer using the other method in next section)
+ There are a lot of tutorials for setting things up for a SSH connection to Pi. Try Google for instance.
+ In order control GPIO pins in python virtual environment: type in command line `sudo python3` to access python virtual environment. From virtual environment type `from gpiozero import *` this imports the gpiozero library. All is set for controlling pins. E.g. try OutputDevice(5).toggle(). You may control each relay by using their BCM numbers (5, 6, 13, 16, 19, 20, 21, and 26 on this relayboard). Exit from virtual environment by pressing Ctrl+C and type `exit()`.

4. Running from remote GPIO
+ GPIO's can be controlled from other computers if you know the Pi's IP. In order to setup your Pi to be controlled from another computer follow next guide: https://github.com/spacefortress3000/remote-GPIO
+ Documentations can be found https://gpiozero.readthedocs.io/en/stable/remote_gpio.html

For further reading: https://gpiozero.readthedocs.io/en/stable/index.html

### Using the tool on Raspberry Pi

1. Open Terminal
2. If git is not installed on your RPi, type `sudo apt install git`
3. `sudo git clone https://github.com/spacefortress3000/ws-relayboard`
4. Install keyboard `sudo pip3 install keyboard`
5. `cd ws-relayboard`
6. Make the main.py executable by `chmod +x directory/to/your/file/main.py` (if you do not know the directory, type `pwd`)
7. `sudo python3 ./main.py`

### Run on reboot

1. `sudo nano /etc/rc.local`
2. `sudo python3 /home/pi/ws-relayboard/main.py`
3. Ctrl+X -> Y -> Enter
4. `sudo reboot`
