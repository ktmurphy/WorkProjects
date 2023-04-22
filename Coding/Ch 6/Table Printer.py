# Write your code here :-)

# table printer - takes list of strings and displays it in a table.

lstOfLsts = [["apples", "bananas", "oranges", "kiwi"], ["dogs", "cats", "bunny", "cow"], ["mice", "men", "of", "and"]]


def printTable(lstOfLsts):
    #find longest word for each group
    longestWord={}
    for i in range(len(lstOfLsts)):
        longestWord[i]=0
        for j in range(len(lstOfLsts[i])):
            if len(lstOfLsts[i][j])>longestWord[i]:
                longestWord[i]=len(lstOfLsts[i][j])


    for j in range(len(lstOfLsts[0])):
        for i in range(len(lstOfLsts)):
            print(lstOfLsts[i][j].rjust(longestWord[i], " "),end = ' ')
        print("\n")
     #for the number of lists there are, print the word at index 0

printTable(lstOfLsts)
