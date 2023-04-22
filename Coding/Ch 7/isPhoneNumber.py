# Write your code here :-)
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdigit():
            return False
    if text[3] != "-":
        return False
    for i in range(4,7):
        if not text[i].isdigit():
            return False
    if text[7] != "-":
        return False
    for i in range(8,12):
        if not text[i].isdigit():
            return False
    return True

message = "Call me at 218-415-0118. I am also available at 712-560-5388"

phoneNumbersFound = 0
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print(f"Phone number is: {chunk}.")
        phoneNumbersFound += 1

if phoneNumbersFound == 0:
    print("No phone numbers found")
else:
    print("Done")

