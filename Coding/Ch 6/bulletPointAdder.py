# Write your code here :-)

# bulletPointAdder.py - copies a list from the clipboard, adds a star and space to the beginning of each line
# adds the newly edited lines to the clipboard, so it's ready to be pasted

# paste text from the keyboard
import pyperclip
text = pyperclip.paste()


#do something to it
text = text.split("\n")
for line in text:
    line = "* " + line

"\n".join(text)

# copy new text to the clipboard
pyperclip.copy(text)
