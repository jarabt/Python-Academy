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

t = TEXTS[1]
text = t.split()

textWithoutDashes = []

for word in text:
    textWithoutDashes.append(word.replace('-', ''))

print(textWithoutDashes)




"""
our_set = set()
for word in t.split():
    if not word.isalnum():
        our_set.add(word[-1])
dirty_chars = "".join(our_set)

cleanTextList = list()

for word in t.split():
    cleanTextList.append(word.strip(dirty_chars))

print(dirty_chars)





counter = 0
for word in cleanTextList:
    flag = True
    for char in list(word):
        if not char.isupper():
            flag = False
    if flag:
        counter += 1



print(counter)
"""
