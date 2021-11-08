# Hey feller! :cowboy_hat_face: This is spacecowboy3000, I'm thrilled you found my repository!

1. This tool is for controlling Raspberry Pi's GPIO's and a WaveShare 8 channel relay board attached to it. The Pi's purpose in this tool is only to control 8 channel relay board. This tool will allow you to control all 8 channel from the Pi itself with keyboard, from command line (and SSH), and from another computer. Sections 2, 3 and 4 will cover these ways of controlling the relay board.
+ Libraries used can be found from requirements.txt. If you do not have the libraries you may install them by typing `pip install` and the `name_of_the_library`.
+ The relay board used in this tool is https://www.waveshare.com/wiki/RPi_Relay_Board_(B). Manual can be found from the depository folder. The code in this repository may not apply to other relay boards since GPIO's used in this tool may not be the same in every board. Best way to find the correct wiring is to look from the board's manual.
+ GPIO's used are 5, 6, 13, 16, 19, 20, 21, and 26 (BCM). Channel numbering go from right to left. For example GPIO 5 controlls channel 1 and GPIO 6 controls channel 2 etc. Please note that all GPIO pin numbers gpiozero library use are Broadcom (BCM) numbering by default. In order to change pin numbering found here: https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering.
+ Configuration are stated in .ini file. You may change the hotkeys, time delay on/off and time delay itself in milliseconds.
  + Hotkeys are by default set to 1,2,3,4... to control channels. Each number pressed refers to the same number of channel. Changing the hotkeys is done in config file. Please note that use only text format. For example ctrl+1
  + Time delay on/off Set value in config file either true if you want delayed on/off or false. Delayed on/off sets the channel on and after certain number of milliseconds turns the channel off.
  + Time delay Set the delay in milliseconds meaning 1 second is 1000 milliseconds. You do the math.

2. In order to control the GPIO's from the Pi itself you need to attach a keyboard or numbad to it.
+ Controlling GPIO's are done by hotkeys which are by default set to 1,2,3,4... Numbers typed refers to channel numbers. For example pressing '1' will do the task for channel 1. You may use your own hotkey for every channel. Hotkey can be changed in .ini file. See previos section.

3. Running commands from command Raspberry Pi's command line or when SSH'ing to Pi
+ There are a lot of tutorials for setting things up for a SSH connection to Pi. Try Google for instance.
+ UPDATE! Run the module containing GPIO commands with next two steps: Type in command line `sudo python3` in order to access python virtual environment. From virtual environment you may run the module by typing `from main import switch` this import the switch function. Hotkeys can be used now as in the section 2.1. For example if configurations are in default setting typing '1' will run toggle to relay channel 1 or delayed on/off if there is stated a delayed on/off in the .ini file. If you are having errors in command line make sure that the tool is in the same folder which the command line states before typing `python3`. If the folder is the same make sure necessary libraries are installed. Python libraries used are found in section 1.1.

4. Running from remote GPIO
+ GPIO's can be controlled from other computers if you know the Pi's IP. In order to setup your Pi to be controlled from another computer follow next guide: https://gpiozero.readthedocs.io/en/stable/remote_gpio.html
+ I will cover this feature later in another repository. Stay tuned!

For further reading: https://gpiozero.readthedocs.io/en/stable/index.html

## Using main.py on Raspberry Pi:

1. Open Terminal
2. If git is not installed on your RPi, type `sudo apt install git`
3. `sudo git clone https://github.com/spacefortress3000/ws-relayboard`
4. Install keyboard `sudo pip3 install keyboard`
5. `cd ws-relayboard`
6. Make the main.py executable by `chmod +x directory/to/your/file/main.py` (if you do not know the directory, type `pwd`)
7. `sudo python3 ./main.py`

## Run on reboot

`sudo nano /etc/rc.local`

`sudo python3 /home/pi/ws-relayboard/main.py`

Ctrl + X -> Y -> Enter

`sudo reboot`
