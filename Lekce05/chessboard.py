num = int(input("Please enter a number: "))
for i in range(num):
    row = ""
    if i%2 == 1:
        for j in range(num):
            row += "# "
    else:
        for j in range(num):
            row += " #"
    print(row)
