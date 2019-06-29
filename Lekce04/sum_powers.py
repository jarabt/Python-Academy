n = int(input("Enter a number: "))
sum = 0

while n:
    sum += n**n
    n -= 1

print("The result is:", sum)
