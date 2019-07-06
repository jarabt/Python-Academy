sentence = 'It was a bright, sunny day in May, and the church bell was just\
 ringing'

aDict = {}

for letter in sentence:
    if letter.isalpha():
        aDict.setdefault(letter, 0)
        aDict[letter] += 1

print(aDict)
