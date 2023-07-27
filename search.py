#! python3
# search.py use: 1: program name 2. search term or "l" for laptop, if no search term 3: 'l' if search term and laptop
# web browser chrome, and 75% zoom
import sys, pyautogui

imageFilesM = {'seeAll':'searchPyMonitor.jpg', 'next':'searchNextM.jpg', 'end': 'searchEndM.jpg'}
imageFilesL = {'seeAll':'searchPyLaptop.jpg', 'next':'searchNextL.jpg', 'end': 'searchEndL.jpg'}

useImageFile = imageFilesM
searchTerm = ''
c = 0.95
scrollLength = -700


if len(sys.argv) == 2:
    if sys.argv[1] == 'l':
        useImageFile = imageFilesL
    else:
        searchTerm = sys.argv[1]
if len(sys.argv) == 3 and sys.argv[2] == 'l':
    useImageFile = imageFilesL
    searchTerm = sys.argv[1]

print('Move mouse to the window you are searching in. Beginning in :', end=''); pyautogui.countdown(3)

def searcher():
    endButton = pyautogui.locateOnScreen(useImageFile['end'], confidence = c)
    while endButton is None:
        seeAllButton = pyautogui.locateOnScreen(useImageFile['seeAll'], confidence = c)
        if seeAllButton is None:
            pyautogui.scroll(scrollLength)
        if seeAllButton is not None:
            pyautogui.click(seeAllButton)
            pyautogui.move(-500,0)
        endButton = pyautogui.locateOnScreen(useImageFile['end'], confidence = c)
    seeAllButton = pyautogui.locateOnScreen(useImageFile['seeAll'], confidence = c)
    while seeAllButton is not None:
        pyautogui.click(seeAllButton)
        pyautogui.move(-500,0)
        seeAllButton = pyautogui.locateOnScreen(useImageFile['seeAll'], confidence = c)
    if searchTerm != '':
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.sleep(.25)
        pyautogui.write(searchTerm)
        pyautogui.sleep(.25)
        pyautogui.press('enter')
    pyautogui.scroll(25000)




while True:
    print('starting')
    searcher()
    endButton = pyautogui.locateOnScreen(useImageFile['end'], confidence = c)
    while endButton is None:
        pyautogui.sleep(3)
        endButton = pyautogui.locateOnScreen(useImageFile['end'], confidence = c)
    nextButton = pyautogui.locateOnScreen(useImageFile['next'], confidence = c)
    if nextButton is not None:
        pyautogui.sleep(2)
        pyautogui.click(nextButton)
        pyautogui.sleep(5)
    if nextButton is None:
        break

