import time
import threading
import keyboard
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
from pynput.keyboard import Controller as KeyboardController, Key

positions = [(1356, 843), (1311, 843), (1270, 843), (1225, 843), (1179, 843), (1135, 843), (1095, 843), (1051, 843), (1002, 843), (956, 843), (915, 843), (870, 843), (825, 843), (786, 843), (740, 843), (738, 886), (781, 886), (828, 886), (869, 886), (914, 886), (960, 886), (1001, 886), (1049, 886), (1092, 886), (1133, 886), (1179, 886), (1223, 886), (1266, 886), (1310, 886), (1353, 886)]

stop_event = threading.Event()
start_event = threading.Event()

mouse = MouseController()
keyboard_controller = KeyboardController()

def perform_clicks():
    for x, y in positions:
        if stop_event.is_set():
            break
        mouse.position = (x, y)
        with keyboard_controller.pressed(Key.shift):
            mouse.click(Button.left)
        time.sleep(0.5)

def key_listener():
    global stop_event, start_event
    while True:
        if keyboard.is_pressed('q'):
            stop_event.set()
            start_event.clear()

print("Hello scrapper, i will do the boring stuff for you just sit and relax,\n"
      "here a little tutorial, press 'o' to store your items in the inventory to the storage,\n"
      "press 'p' to quick buy in the market (automated left-click + enter). To stop the script press 'q'.\n"
      "Happy scrapping from Pivot.")


key_thread = threading.Thread(target=key_listener)
key_thread.start()

def market_click_buy():
    while True:
        if stop_event.is_set():
            break

        mouse.click(Button.left)
        with keyboard_controller.pressed(Key.enter):
            pass
        time.sleep(0.2)

while True:
    try:
        if keyboard.is_pressed('o') and not start_event.is_set():
            start_event.set()
            stop_event.clear()
            perform_clicks()
        if keyboard.is_pressed('p') and not start_event.is_set():
            start_event.set()
            stop_event.clear()
            market_click_buy()
    except KeyboardInterrupt:
        stop_event.set()
        break

key_thread.join()
