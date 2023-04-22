# Write your code here :-)
## To do: install pyperclip and other modules; learn Appendix B and try

#! python3
# mclip.py - a multi-clipboard
import sys, pyperclip
TEXT = {"tfr": "Thank you so much for registering! I'll be presenting your bio to my client today, and then I will be in touch if the client chooses to proceed with the call.", "call": "Great to hear! Would you provide a few times that work today or tomorrow and your phone number? I'll confirm the time and call you then."}

if len(sys.argv) < 2:
    print("To use this program, type \'mclip.py [keyphrase]\'")
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for \'" + keyphrase + "'\ has been copied")
else:
    print("There is no text for \'" + keyphrase + "'.")


