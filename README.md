# ENGR 107 Team 2 Rover
ENGR 107 Team 2 Rover Web Interface, to run on a Pi Zero and control the vehicle's motors.

# Program Usage
**This guide is written for operation on a Pi running Raspbian or Debian, and some commands may need to be substituted on other systems** *(such as `python` or `py` in place of `python3`)*

Requirements: Python 3 and the Python module `aiohttp`. 

*(Install these on the Pi using `sudo apt install python3`, then `sudo apt install python3-pip`, and finally `pip3 install aiohttp`)*

In a terminal, simply type
```
$ python3 server.py
```

Next, navigate with a web browser to `<the Pi's IP>:8080`, replacing `<the Pi's IP>` with the IP address of the Pi.

You should find yourself on a webpage with a button. Pressing this will toggle the GPIO pin, which can be used to trigger a relay or other device such as an LED.

# Hardware Usage
This program controls GPIO pin 17, which is Pin 11 on the Pi. A helpful guide as to the pins' locations on the board can be found at https://pinout.xyz/.