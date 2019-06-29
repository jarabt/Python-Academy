n = int(input("Zadej počet opakování: "))
s = input("Zadej string: ")

l = s.split()
result = []

while l:
    word = l.pop(0)
    word = [word] * n
    result = result + word

result = " ".join(result)

print(result.lstrip())
