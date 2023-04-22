#! python3
# busyBeaver.py - looks busy
import pyautogui, time, datetime
breakTime = datetime.datetime.now()+datetime.timedelta(hours = 1)
print(breakTime)
while datetime.datetime.now() < breakTime:
    time.sleep(10)

print('Hit ctrl+c to get back to it!')
try:
    while True:
        time.sleep(5)
        for i in range(2):
            pyautogui.move(100,0, duration=0.25)
            pyautogui.move(0, 100, duration= 0.25)
            pyautogui.move(-100,0, duration=0.25)
            pyautogui.move(0, -100, duration=0.25)
except KeyboardInterrupt:
    print('Welcome back!')
