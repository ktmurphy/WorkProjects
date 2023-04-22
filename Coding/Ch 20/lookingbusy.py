#! python3
# busybeaver.py - looks busy
import pyautogui, time
print('Hit any key to get back to it!')
try:
    while true:
        time.sleep(60)
        for i in range(2):
            pyautogui.move(100,0, duration=0.25)
            pyautogui.move(0, 100, duration= 0.25)
            pyautogui.move(-100,0, duration=0.25)
            pyautogui.move(0, -100, duration=0.25)
except KeyboardInterrupt:
    print('Welcome back!')
