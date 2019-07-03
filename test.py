numbers = [321,45,32,12,54]
for index, number in enumerate(numbers):
    if index % 2 == 0:
        print(number, ':', number**2)


print(enumerate(numbers))
