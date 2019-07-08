def my_function(x, y):
    sum = 0
    for n in range(x, y):
        sum += n
    return sum

a = int(input("Zadej počátek: "))
b = int(input("Zadej konec: "))

print(my_function(a, b))
