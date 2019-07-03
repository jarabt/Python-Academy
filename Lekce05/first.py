names = ['Jakub', 'Jana', 'Petr', 'Klara']
sumOfAllLetters = 0


for x in names:
    print(x)
    if x[0] == "J":
        print("With \"J\" begins:", x)
    sumOfAllLetters += len(x)

print(sumOfAllLetters)
