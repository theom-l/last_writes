import openai
import requests
import time
import subprocess
import RPi.GPIO as GPIO
import os

from module.thermo_printer import PrinterManager
from module.interface import InterfaceManager

# defining state machine states
WELCOME = 0
WAITING_FOR_DEVICE = 1
DEVICE_LOADED = 2
READING_DATA = 3
GENERATING_RESPONSE = 4
DISPLAYING_RESPONSE = 5
PRINTING_RESPONSE = 6
THANK_YOU = 7

# init variables
program_state = WELCOME
next_state = WELCOME
is_loading_state = False

# init variables from modules
im = InterfaceManager(gpt3_response="init")
pm = PrinterManager()

# GPIO setup


def init():
    print('initializing')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    im.flush_screen()
    im.display_loading()
    time.sleep(2)
    im.flush_screen()
    im.display_ui(program_state)

# move state


def jump_to_next_state():
    global program_state
    global next_state
    global is_loading_state
    if next_state < 4:
        next_state += 1
    else:
        next_state = 0


# program loop
def loop():
    # if next state is advanced (user clicked the advance button)
    global program_state
    global next_state
    if program_state != next_state:
        # loading transition
        im.flush_screen()
        im.display_loading()
        time.sleep(1)

        # display new interface for the new state
        im.flush_screen()
        im.display_ui(next_state)
        program_state = next_state
    GPIO.wait_for_edge(26, GPIO.RISING)
    jump_to_next_state()
    time.sleep(1)


def main():
    init()
    while True:
        loop()
        time.sleep(0.1)


if __name__ == "__main__":
    main()
