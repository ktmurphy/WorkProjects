# Write your code here :-)
import re
numRegex = re.compile(r'(^\d{1,3})(,\d{3})+')

search = numRegex.search('443,234')
if search != None:
    print(search.group())
else:
    print("No Matches")

nameRegex = re.compile(r'^[A-Z][a-z]+\sWatanabe$')
searchName = nameRegex.search('John Watanabe')
if searchName != None:
    print(searchName.group())
else:
    print("No Matches")


listRegex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.',re.I)
listName = listRegex.search('Robocop throws APples.')
if listName != None:
    print(listName.group())
else:
    print("No Matches")
