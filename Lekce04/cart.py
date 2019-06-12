"""
Projekty posílejte na:mates.sveda@gmail.com
od seste lekce konzultace?
"""




cart = {}
flag = True
suma = 0

while flag == True:
    vstup = input("Zadej cenu (pokud chces koncit, dej pouze enter): ")
    if vstup == "":
        flag = False
    else:
        key = input("Zadej název: ")
        cart[key] = float(vstup)
        suma += cart[key]
print(cart)
print(suma)
