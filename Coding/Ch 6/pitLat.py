# Write your code here :-)
# pigLat.py - translates from English to pig latin
while True:
    print ("Enter the English message to translate into Pig Latin:")

    message = input()

    VOWELS = ["a", "e", "i", "o", "u", "y"]


    # input split into single words
    pigLatinMessage = []


    # if/then to see how to handle, handle: upper/lower, consonant clusters, spaces, punctuation

    #start to modify the words
    for word in message.split():
        #punctuation/space preservation - beginning of word
        punctuationAndSpaces = ''
        while len(word) > 0 and not word[0].isalpha():
            punctuationAndSpaces += word[0]
            word =word[1:]
        if len(word) == 0:
            pigLatinMessage.append(punctuationAndSpaces)

        #punctuation/space preservation - end of word
        endPunctAndSpaces = ''
        while not word[-1].isalpha():
            endPunctAndSpaces += word[-1]
            word = word[:-1]


        #remember if word is uppercase or titlecase
        wasUpper = word.isupper()
        wasTitle = word.istitle()

        #move to lower for processing
        word = word.lower()

        #separate consonants
        prefixConsonants = ''
        while len(word) > 0 and word[0] not in VOWELS:
            prefixConsonants += word[0]
            word = word[1:]

        if len(prefixConsonants) != 0:
            word = word + prefixConsonants + "ay"
        else:
            word = word + "yay"

        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()

        pigLatinMessage.append(punctuationAndSpaces + word + endPunctAndSpaces)
    # join back together
    print(' '.join(pigLatinMessage))




