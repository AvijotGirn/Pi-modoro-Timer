# Pi-modoro-Timer
A Pomodoro timer program implemented using a Raspberry Pi Pico &amp; Micropython (Thonny IDE). 

## Features
There are 3 preset times or "session" lengths:
- 1 min Work / 1 min Break   **Use for Testing/Debugging**
- 35 min Work / 10 min Break
- 45 min Work / 15 min Break
> During the Selection Screen, the User must wait until the screen prompts them to hold the button for their selection, this is done to account for limited screen space on the 1602 LCD module and the number of options available

There is pause functionality implemented which simply stops the timer when the STOP button is pushed, and resumes when the OK Button is pushed.

The Work/Break sessions will run twice (i.e. 2 Work Sessions and 2 Breaks Total), however this can be changed very easily bu adjusting the range of the for loop in main.py

# Prerequisites 

## Circuit
- Raspberry Pi Pico (or equivalent): Eg. https://www.sunfounder.com/products/pico-starter-kit 
- Some simple components (generally will be included as part of a microcontroller Kit)
  - Push Button x3
  - 10 kOhm Resistor x3
  - Jumper Cables M2M (varies depending on circuit & size of breadboard)
  - Jumper Cables M2F x4 (Connecting LCD Module)

## Software
- Thonny IDE (with Raspberry Pi device setup)
- App.py AND lcd1602.py **must** be loaded onto the Pico before running the program
  - Note that lcd1602.py is a provided class (i.e. I did not write it), however I have provided it as part of the code 

# Circuit Diagram
## LCD Connection 
Image from Sunfoudner Thales Kit Docs/Tutorial: https://docs.sunfounder.com/projects/thales-kit/en/latest/introduction_to_raspberry_pi_pico.html
![LCD Module Connection](/Images/Lcd1602.png?raw=true "LCD Connection")

## Schematic for PBs
The Following are schematics for the MISC, OK, and STOP push buttons (respectively) as they are referenced in the code.
![PB1](/Images/PB_MISC.png?raw=true "MISC Push Button")
![PB2](/Images/PB_OK.png?raw=true "OK Push Button")
![PB3](/Images/PB_STOP.png?raw=true "STOP Push Button")

## My Circuit Setup 
**Note:** It is not necessary to have 2 breadboards or as many wires, mine was done this way for visualization purposes and ease of access to the buttons.
![c1](/Images/circuit1.png?raw=true "My Circuit Setup")
![c2](/Images/circuit2.png?raw=true "My Circuit Setup Im 2")

# Running 
1) Setup Circuit
2) Load App.py and lcd1602.py onto the Pico
  - On Thonny, after connecting Pico: File >> Save As >> Raspberry Pi Pico >> App.py
  - Repeat for lcd1602.py
3) Either run main.py from Thonny IDE or Upload main.py to the Pico as well (this way no computer is needed to run the program, just provide the pico power, and it will automatically run main.py when plugged in)
