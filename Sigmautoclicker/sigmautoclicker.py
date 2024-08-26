import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

key = input("What key should start SIGMAUTOCLICKER?:  ")
cps_num = input("Type a number like 0.0001, add more 0s for faster cps:  ")
cps = float(cps_num)
print("")
print("SIGMAUTOCLICKER is now in action, press the",key,"key to toggle it on and off")
print("")
print("")
print("Made by Sigma SD")



TOGGLE_KEY = KeyCode(char=key)
clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(cps)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

