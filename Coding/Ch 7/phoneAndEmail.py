#copy text to clipboard, run program to search for phone numbers and email, and replace text on clipboard with phone numbers and emails.

import re, pyperclip


# Use Pyperclip to copy and paste


# Create regexes
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? #area code
(-|\s|\.|\s)    #separator
(\d{3})       #first three digits
(-|\s|\.)     #separator
(\d{4})        #first three digits
(\s*(Ext.|x|ext.|ext)\s*(\d{2,5}))?
)''', re.VERBOSE)

emailRegex = re.compile(r'\S+@\w+\.\w+')


#pyperclip.paste will get a string value of the text on the clipboard. Paste returns text from clipboard
text = str(pyperclip.paste())


#Find matches
matches = []

for groups in phoneRegex.findall(text):
    if groups[1] !='':
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    else:
        phoneNum = '-'.join([groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]

    matches.append(phoneNum)
for address in emailRegex.findall(text):
    matches.append(address)


#format matches into string
if len(matches) > 0:
    printable = "\n".join(matches)
    pyperclip.copy(printable)
    print("Copied to clipboard:")
    print(printable)
#display if no matches found
if len(matches) == 0:
    print("No matches found")







