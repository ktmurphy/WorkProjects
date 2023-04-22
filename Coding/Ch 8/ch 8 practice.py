# Write your code here :-)
import pyinputplus as pyinp
#creating custom input checker, tool
def addsUpToTen(numbers):
    #returns a list based on the items in the iterable
    numbersList = list(numbers)
    #enumerate creates a list of the items in a list with an index in front like [(0, 5), (1,3)]
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))

    print('Great Job')
    return int(numbers)

response = pyinp.inputCustom(addsUpToTen, prompt="Enter numbers that add to Ten: ")


