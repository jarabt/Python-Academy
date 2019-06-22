'''
author = Jaroslav Tesař
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

print('Hello user!')
enteredU = input('Give me your username: ')
enteredP = input('Now password please: ')
registered = {'bob':'123', 'ann':'pass123', 'mike':'password123',\
        'liz':'pass123'}
if registered.get(enteredU, 0) != enteredP:
    print('Your username or password is not correct!!!')
else:
    textChoice = input('Please choose text number (1-3): ')
    chosenText = TEXTS[int(textChoice) - 1]
    print()

    # Put dashes away
    textListWithoutDashes = []
    for word in chosenText.split():
        textListWithoutDashes.append(word.replace('-', 'x'))

    # Put dirty chars away
    our_set = set()
    for word in textListWithoutDashes:
        if not word.isalnum():
            our_set.add(word[-1])
    dirty_chars = "".join(our_set)
    cleanTextList = list()
    for word in textListWithoutDashes:
        cleanTextList.append(word.strip(dirty_chars))

    print('Number of words:', len(cleanTextList))
    counterCap = 0
    counterUpper = 0
    counterLower = 0
    counterNum = 0
    sumOfNum = 0.0
    wordLengthArray = [0] * 15
    for word in cleanTextList:
        if word[0].isupper():
            counterCap += 1
        if word.isalpha():
            if word.isupper():
                counterUpper += 1
            elif word.islower():
                counterLower += 1
        elif word.isnumeric():
            counterNum += 1
            # sum of all the numeric "words"
            sumOfNum += int(word)
        # the frequencies of word lengths
        wordLengthArray[len(word)-1] += 1
    print('Number of words starting with capital letter:', counterCap)
    print('Number of uppercase words:', counterUpper)
    print('Number of lowercase words:', counterLower)
    print('Number of numeric words:', counterNum)
    # Number of words with the same length
    print()
    print('Depicting the frequencies of word lengths in the text:')
    for index, length in enumerate(wordLengthArray):
        print(index + 1, '*' * length, length)
    print()
    print('The sum of all the numeric "words":', sumOfNum)
