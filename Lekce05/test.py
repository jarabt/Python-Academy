
j = 8


for i in range(4):
        print("# " + str(j) + 4 * "|#| " + "|")
        print(17 * "-")
        j -= 1
        print( "# " + str(j) + 4 * "| |#" + "|")
        print(17 * "-")
        j -= 1

print(" A B C D E F G H")









"""
lst = list (range(10))
for i in range(10):
    lst[i] = lst[i] + 1
print(lst)



# Zadany viceradkovy text

TEXT = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''


listtext = TEXT.split()
dirty_chars = "".join(our_set)

for index, word in enumerate(listtext):
    if word.strip(dirty_chars) == vstup:
        print(index, vstup)

#moje:
listtext = TEXT.split()
vstup = input("Zadej znak: ")
for word in listtext:
    i = listtext.index(word)
    if not word.isalnum():
        word = word[:-1]
    if word == vstup:
        print ("ano")
        print(i)



    nlisttext.append(word)

vstup = input("Zadej znak: ")

for word in nlisttext:
    if word == vstup:
        print ("ano")
        print(nlisttext.index(word))

vstup = input("Zadej znak: ")
nlisttext = list()

for word in listtext:
    if word == vstup:
        print ("ano")


print(listtext)



for word in TEXT.split():
    if not word.isalnum():
        myset.add(word[-1])

vstup = input("Zadej znak: ")
pouzeslova  =

if vstup in myset:
    print("ano")


print (myset)
'''
"""
