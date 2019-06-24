cart = []
sum = 0
flag = True


while flag:
    item = input("Zadej cenu: ")
    cart.append(float(item))
    answer = input("Zmáčkni enter pro pokračování, 'q' pro konec: ")
    if answer == "q":
        flag = False

i = 0
repeat = True
while repeat:
    index = i % len(cart)
    print(cart[index])
    answer = input("For another item press enter, to stop press 'q'")
    if answer == "q":
        repeat = False
    else:
        i += 1

i = 0
while i < len(cart):
    sum += cart[i]
    i += 1

print(cart)
print(sum)
