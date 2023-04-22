#! python3
import pyautogui, time, webbrowser
submitAnotherLink = (518,518)
#webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform')
#time.sleep(5)
formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'}]
pyautogui.PAUSE = 3
print('Ensure that the browser window is active and the form is loaded.')

for person in formData:
    print('> 1 Second Pauseto press CTRL-C<')
    time.sleep(2)
    print('Entering %s\'s Info...' % (person['name']))
    pyautogui.click(100,200)
    time.sleep(1)
    pyautogui.write(['\t', '\t', '\t', '\t'])
    pyautogui.write(person['name'] + '\t')
    pyautogui.write(person['fear'] +'\t')
    if person['source'] == 'wand':
        pyautogui.write(['down', 'enter', '\t'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', 'enter', '\t'], 0.5)

    if person['robocop'] == 1:
        pyautogui.write([' ', '\t'], 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t', '\t'], 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t', '\t'], 0.5)
    pyautogui.write(person['comments']+'\t')
    time.sleep(0.5)
    pyautogui.press('enter')
    print('Submitted Form for %s...' % person['name'])
    time.sleep(5)
    pyautogui.click(submitAnotherLink)
