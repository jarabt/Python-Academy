#asi funguje moje...
"""
j = 8


for i in range(4):
        print("# " + str(j) + 4 * "|#| " + "|")
        print(21 * "-")
        j -= 1
        print( "# " + str(j) + 4 * "| |#" + "|")
        print(21 * "-")
        j -= 1

print("    A B C D E F G H")
"""

##### jeho
sym = ["#"," "]
size = 20
desk = []

# pro cislo radku a radek
for r, row in enumerate(range(size)):
    line = []
    # pro cislo bunky a bunku
    for c, cell in enumerate(range(size)):
        # mi nahrej do linie symbol z listu 'sym', ktery vyberes podle indexu
        # index bude zbytek souctu cisla radku a bunky vydeleny delkou listu 'sym'
        line.append(sym[(r + c) % len(sym)])
    # vystiskni mi linii, kterou si napojim do stringu
    desk.append("".join(line))


print("\n".join(desk))
