n = int(input("Please enter length: "))
c = input("Enter a char: ")

pole = [c, " "]

for i in range(n):
    row = ""
    for j in range(n):
        row += pole[(i + j) % len(pole)]
    print(row)
