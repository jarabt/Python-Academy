num = int(input("Enter a number: "))

myList = []

for i in range(num):
    row = []
    for j in range(num):
        row.append(j)
    myList.append(row)

print(myList)
