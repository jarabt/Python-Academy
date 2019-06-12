DB_POTRAVINY = {
        'P1': {'produkt': 'Chleba', 'cena': 25, 'Pocet': 100},
        'P2': {'produkt': 'Pomeranc', 'cena': 15, 'Pocet': 100},
        'P3': {'produkt': 'Kecup', 'cena': 35, 'Pocet': 100},
        'P4': {'produkt': 'Orbitky', 'cena': 13, 'Pocet': 100},
        'P5': {'produkt': 'Mleko', 'cena': 30, 'Pocet': 100},
        }
i = 1
seznam_potravin = []

while "P"+str(i) in DB_POTRAVINY.keys():
    seznam_potravin.append([DB_POTRAVINY["P"+str(i)]["produkt"],\
    (DB_POTRAVINY["P"+str(i)]["cena"])])
    print("PRODUKT: " + DB_POTRAVINY["P"+str(i)]["produkt"] + ", CENA: " +\
    str(DB_POTRAVINY["P"+str(i)]["cena"]))
    i += 1

kosik = {}

flag = True
while flag:
    potravina = input("Zadej potravinu: ")
    mnozstvi = int(input("Zadej mnozstvi: "))
    dotaz = input("Chces pokracovat (enter ano, q ne)? ")
    i = 0
    while i < len(seznam_potravin):
        if seznam_potravin[i][0] == potravina:
            kosik[potravina] = 

    if dotaz == "q":
        flag = False




print(seznam_potravin)
