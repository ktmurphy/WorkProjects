# Write your code here :-)
#! python3
# madlib.py - reads a text file and lets the user add their own text for missing Adjectives, Nouns, Adverbs, or Verbs

import pyinputplus as pyin
import re

# when this program is not in Mu, would update this to sys args where you could put in the file as an argument
# open and read file
madlibFile = open('madlib.txt', 'r')
madlibContent = madlibFile.read()

# create and open file for new sentence after inputs
generatedSentence = open('madlibfinished.txt', 'w')

# create regex for words
wordTypesRegex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

# search madlibfile for those words, make list
requiredWords = wordTypesRegex.findall(str(madlibContent))

# loop through each word in list and get replacement word,
for word in requiredWords:
    replacementWord = pyin.inputStr(prompt = (f'Enter an {word.lower()}\n'))
    madlibContent = wordTypesRegex.sub(replacementWord, madlibContent, 1)

# display madlib content and write to file
print(madlibContent)
generatedSentence.write(madlibContent)

# close files
madlibFile.close()
generatedSentence.close()


