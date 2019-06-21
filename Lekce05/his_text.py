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

our_set = set()
for word in TEXT.split():
    if not word.isalnum():
        our_set.add(word[-1])
dirty_chars = "".join(our_set)

listtext = TEXT.split()

vstup = input("Zadej hledané slovo: ")

for index, word in enumerate(listtext):
    if word.strip(dirty_chars) == vstup:
        print(index, vstup)
