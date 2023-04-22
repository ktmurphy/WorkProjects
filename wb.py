#! python3
# whiteBoxWriter.py - renamed wb.py - writes white box note and gets bio email ready to send

# modules needed: sys, re, bs4, docx, pyautogui, time, pyperclip

import sys, re, bs4, pyautogui, time, pyperclip, docx
# 1. Accepts input for project subject
'''
if len(sys.argv) < 2:
    print('Usage: whiteBoxWriter.py subjectOfProject')
    sys.exit()

subjectOfProject = ' '.join(sys.argv[1:])

# 2. Makes selections
pyautogui.click('''
# 3. Writes Greeting and initial sentences - based on some template options or quantity of bios (Initial bios, 1, 2, or more)
# 4. Writes each WB note
# 5. Writes closing
# 6. Formats
# 7. Includes each VQA
# 8. Pop up box when white box is ready

