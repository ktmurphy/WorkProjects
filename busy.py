#! python3
# busyBeaver.py - renamed busy.py - looks busy
# usage: busy.py optional: 'break' - meaning that you are going on lunch. Otherwise, loop will start right away.
import pyautogui, time, datetime, sys

print('Hit ctrl+c to get back to it!')

if len(sys.argv) == 2 and sys.argv[1] == 'break':
    print('Enjoy your break!')
    breakTime = datetime.datetime.now()+datetime.timedelta(hours = 1)
    print('Break ends: ', breakTime)
    while datetime.datetime.now() < breakTime:
        time.sleep(30)
    pyautogui.click()
    print('Break over')

try:
    while True:
        time.sleep(60)
        for i in range(2):
            pyautogui.move(100,0, duration=0.25)
            pyautogui.move(0, 100, duration= 0.25)
            pyautogui.move(-100,0, duration=0.25)
            pyautogui.move(0, -100, duration=0.25)
            pyautogui.click()
            pyautogui.click()
except KeyboardInterrupt:
    print('Welcome back!')
