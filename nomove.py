import pyautogui
from pynput.keyboard import Key, Listener
from threading import Thread

# set state of loop to false
active = False

# loop that moves mouse back to center every 0.1 seconds (default speed)
def active_loop():
    while active:
        #print(pyautogui.position())    # position of mouse currently

        # move mouse roughly to the center (1440p screen)
        pyautogui.moveTo(1300, 700)

def on_release(key):
    #print(key)     # print key info
    
    # key input to start of script
    if key == Key.page_down:
        global active
        t1 = Thread(target = active_loop)   # multithreaded to run 2 loops at the same time
        
        # set the state of active
        if active:
            print("DISABLED")
            active = False
        else:
            print("ENABLED")
            active = True
            t1.start()  # start thread
    
    # key input to end script
    if key == Key.end:
        print("Exiting")
        return False

print("Press 'Page Down' to start/pause script\nPress 'End' to end script")

# listener loop that detects keyboard inputs, even in the background
with Listener(on_release=on_release) as listener:
    listener.join()