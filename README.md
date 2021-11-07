# Hey feller! :cowboy_hat_face: This is spacecowboy3000, I'm thrilled you found my repository!

1. This tool is for controlling Raspberry Pi's GPIO's and a WaveShare 8 channel relay board attached to it. The Pi's purpose in this tool is only to control 8 channel relay board and therefore may not be suitable for desktop use because of the hotkeys in this tool (see section 2.1). This tool will allow you to control all 8 channel from the Pi itself with keyboard, from command line (and SSH), and from another computer. Sections 2, 3 and 4 will cover these ways of controlling the Pi.
1.1. Libraries used: configparser, gpiozero, time, and keyboard. If you do not have the libraries you may install them by typing 'pip install' and the name of the library. In next sections there may be some other libraries not listed here. You may install the libraries accordingly showed in this section. Libraries and versions can be found from requirements.txt.
1.2. The relay board used in this tool is https://www.waveshare.com/wiki/RPi_Relay_Board_(B). Manual can be found from the folder. You may also use other relay boards. Note that the GPIO's used in this tool may not be the same in every board. Best way to find the correct wiring is to look from the board's manual.
1.3. GPIO's used are 5, 6, 13, 16, 19, 20, 21, and 26 (BCM). Channel numbering go from right to left. For example GPIO 5 controlls channel 1 and GPIO 6 controls channel 2 etc. Please note that all GPIO pin numbers gpiozero library use are Broadcom (BCM) numbering by default. In order to change pin numbering found here: https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering.
1.4. Configuration are stated in .ini file. You may change the hotkeys, time delay on/off and time delay itself in milliseconds.
1.4.1. Hotkeys are by default set to 1,2,3,4... to control channels. Each number typed refers to the same number of channel. Changing the hotkeys are done in config file. Please note that use only text format. For example 'ctrl+1'
1.4.2. Time delay on/off Set value in config file either true if you want delayed on/off or false. Delayed on/off sets the channel on and after certain number of milliseconds turns the channel off.
1.4.3. Time delay Set the delay in milliseconds meaning 1 second is 1000 milliseconds. You do the math.

2. In order to control the GPIO's from the Pi itself you need to attach a keyboard or numbad to it.
2.1. Controlling GPIO's are done by hotkeys which are by default set to 1,2,3,4... Numbers typed refers to channel numbers. For example typing '1' will do the task for channel 1. You may use your own hotkey for every channel. Hotkey can be changed in .ini file. See section 1.4.

3. Running commands from command Raspberry Pi's command line or when SSH to Pi
3.1. There are a lot of tutorials for setting things up for a SSH connection to Pi. Try Google for instance.
3.2. Run the module containing GPIO commands with next two steps: Type in command line 'python3' in order to access python virtual environment. From virtual environment you may run the module by typing 'import RPi_Relay_ Board' this will run the tool. Hotkeys can be used now as in the section 2.1. For example if configurations are in default setting typing '1' will run toggle to relay channel 1 or delayed on/off if there is stated a delayed on/off in the .ini file. If you are having errors in command line make sure that the tool is in the same folder which the command line states before typing 'python3'. If the folder is the same make sure necessary libraries are installed. Python libraries used are found in section 1.1.

4. Running from remote GPIO
4.1. GPIO's can be controlled from other computers if you know the Pi's IP. In order to setup your Pi to be controlled from another computer follow next guide: https://gpiozero.readthedocs.io/en/stable/remote_gpio.html
4.2. To the python tool you are making or in virtual environment you need first import the PiGPIOFactory library by typing 'from gpiozero.pins.pigpio import PiGPIOFactory'. Then you need to define the a variable which calls the GPIO on Pi by typing 'myfactory = PiGPIOFactory(host='192.168.1.x')'. Change the IP address to match the Raspberry Pi's IP address. factory here is the variable and you may change it to whatever you like. Make sure the variable is the same than in the next step. Finally type 'ch1 = OutputDevice(5, pin_factory=myfactory)'. Now you may type 'ch1.on()' and the GPIO 5 (BCM) will be on.

For further reading: https://gpiozero.readthedocs.io/en/stable/index.html

## Using main.py on Raspberry Pi:

1. Open Terminal
2. If git is not installed on your RPi type `sudo apt install git`
3. `git clone https://github.com/spacefortress3000/ws-relayboard`
4. Install keyboard `sudo pip3 install keyboard`
5. `cd ws-relayboard`
6. Make the main.py executable by `chmod +x directory/to/your/file/main.py` (if you do not know the directory, type `pwd`)
7. `sudo python3 ./main.py`
