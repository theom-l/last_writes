from cgi import print_arguments
import curses
import os
import time
from module.gpt3 import GPT3_Api
from module.thermo_printer import PrinterManager

# defining state machine states
WELCOME = 0
WAITING_FOR_DEVICE = 1
DEVICE_LOADED = 2
READING_DATA = 3
GENERATING_RESPONSE = 4
DISPLAYING_RESPONSE = 5
PRINTING_RESPONSE = 6
THANK_YOU = 7

gpt3 = GPT3_Api()
pm = PrinterManager()

# add state variables


class InterfaceManager:
    gpt3_response = "init"

    def __init__(self, gpt3_response):
        super().__init__()
        self.interface = ''
        self.gpt3_response = gpt3_response

    def flush_screen(self):
        os.system("clear")

    def display_loading(self):
        print('loading')

    def display_ui(self, state):
        if state == 0:
            print(
                "\nWelcome to your Last Writes machine.")
            time.sleep(2)
            print(
                "\nIt's always a great time to let go of your old devices and recycle them.")
            time.sleep(3)
            print(
                "\nLet's help them pass on to the next phase of their lifecycle together.")
            time.sleep(3)
            print("\nPress the red button to continue.\n")
        if state == 1:
            print(
                "Waiting for device to connect.")
            time.sleep(1)
            print("\nConnect device and push the red button to proceed.\n")
        if state == 2:
            print("USB Device from Seagate loaded.")
            time.sleep(1)
            print("\nReading data.\n")
            time.sleep(4)
            os.system("clear")
            print("\nfall 2012 classes")
            time.sleep(1)
            print("\nBorn Jan 14, 2010")
            time.sleep(1)
            print("\nDevice total size: 15.98 GB")
            time.sleep(1)
            print("\nDevice space used: 9.11 GB")
            time.sleep(1)
            print("\nPress the button to generate an obituary for fall 2012 classes.\n")
        if state == 3:
            self.gpt3_response = gpt3.gpt3_request()
            print(self.gpt3_response)
            time.sleep(3)
            print("\nPress the button to print.\n")
        if state == 4:
            pm.print(self.gpt3_response)
            pm.print("Please recycle me at your nearest e-waste recycling center:\n\nEvolution E-Cycling\n2235 Mary St. Pittsburgh, PA\n(412) 390-3450\n")
            print("\nThanks for using your Last Writes machine. Please recycle.\n")



def main():
    stdscr = curses.initscr()
    pad = curses.newpad(100, 100)
    for y in range(0, 99):
        for x in range(0, 99):
            pad.addch(y, x, ord('a') + (x*x+y*y) % 26)
    pad.refresh(0, 0, 5, 5, 20, 75)


if __name__ == "__main__":
    main()
