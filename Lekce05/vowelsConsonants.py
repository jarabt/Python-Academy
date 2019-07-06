
"""
#moje:

givenS = "a speech sound that is produced by comparatively open \
configuration of the vocal tract"

givenS = givenS.replace(" ","")

numOfVowels = 0

vowels = "aeiouy"

for char in givenS:
    if char in vowels:
        numOfVowels += 1

print("Vowels:", numOfVowels, "\nConsonants:", len(givenS) - numOfVowels)
"""

#jejich:
vowels = set('aeiouy')

letters = set()
# 1.
letter_a = 97
letter_z = 123

# 3.
for num in range(letter_a, letter_z):
    # 2.
    letters.add(chr(num))  #chr() je opak ord()

# 4.
consonants = letters - vowels

counts = {'cons':0,'vows':0}

sentence = 'a speech sound that is produced by comparatively open configuration of the vocal tract'

for char in sentence:
    if char.isalpha():
        if char.lower() in vowels:
            counts['vows'] = counts['vows'] + 1
        else:
            counts['cons'] = counts['cons'] + 1

print('No. consonants: ' + str(counts['cons']) + ' | No. vowels: ' + str(counts['vows']))
