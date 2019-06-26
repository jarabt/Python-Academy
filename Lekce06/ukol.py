# Vyscrapovane informace z realitek
# Vlozime jej jako viceradkovy retezec
DATA_SCRAP = '''
byt 0001,55 m2,Olomouc,ul.Heyrovského,
byt 0003,65 m2,Olomouc,ul.Novosadský dvůr,
byt 0004,75 m2,Olomouc,ul.Wolkerova,
byt 0004,68 m2,Olomouc,ul.Zikova,
byt 0001,36 m2,Olomouc,ul.Nová Ulice,
byt 0003,46 m2,Olomouc,ul.Nové sady,
byt 0004,75 m2,Olomouc,ul.Nová Ulice,
byt 0003,42 m2,Olomouc,ul.Nová Ulice,
byt 0005,107 m2,Olomouc,ul.Nová Ulice,
byt 0003,74 m2,Olomouc,ul.Uničovská,
byt 0003,42 m2,Olomouc,ul.Nešverova,
byt 0002,55 m2,Olomouc,ul.Dělnická,
byt 0004,59 m2,Olomouc,ul.Zirmova,
byt 0007,92 m2,Olomouc,ul.Nová Ulice,
byt 0002,52 m2,Olomouc,ul.Nová Ulice,
byt 0004,76 m2,Olomouc,ul.Nová Ulice,
byt 0002,81 m2,Olomouc,ul.Nová Ulice,
byt 0003,64 m2,Olomouc,ul.Za vodojemem,
byt 0007,113 m2,Olomouc,ul.Jihoslovanská,
byt 0005,94 m2,Olomouc,ul.Uničovská,
byt 0003,42 m2,Olomouc,ul.Rošického,
byt 0003,75 m2,Olomouc,ul.Rošického,
byt 0004,48 m2,Olomouc,ul.Handského,
byt 0004,68 m2,Olomouc,ul.Komenského,
byt 0003,61 m2,Olomouc,ul.Jarmily Glazarové,
byt 0004,39 m2,Olomouc,ul.Přichystalova,
byt 0003,70 m2,Olomouc,ul.Foerstova,
byt 0005,61 m2,Olomouc,ul.Nová Ulice,
byt 0007,88 m2,Olomouc,ul.Nová Ulice,
byt 0003,92 m2,Olomouc,ul.U cukrovaru,
byt 0003,56 m2,Olomouc,ul.U cukrovaru,
byt 0004,56 m2,Olomouc,ul.Paseka,
byt 0002,74 m2,Olomouc,ul.Rokycanova,
byt 0007,116 m2,Olomouc,ul.U cukrovaru,
byt 0004,59 m2,Olomouc,ul.Řezáčova,
byt 0004,100 m2,Olomouc,ul.Libušina,
byt 0003,64 m2,Olomouc,ul.Řezáčova,
byt 0001,33 m2,Olomouc,ul.Libušina,
byt 0006,87 m2,Olomouc,ul.Černá cesta,
byt 0007,95 m2,Olomouc,ul.Kaštanová,
byt 0003,74 m2,Olomouc,ul.Nová Ulice,
byt 0003,75 m2,Olomouc,ul.Nová Ulice,
byt 0004,86 m2,Olomouc,ul.Hněvotínská,
byt 0002,67 m2,Olomouc,ul.Polská,
byt 0007,120 m2,Olomouc,ul.Dvořákova,
byt 0004,90 m2,Olomouc,ul.Dvořákova,
byt 0004,86 m2,Olomouc,ul.Nová Ulice,
byt 0003,75 m2,Olomouc,ul.Nešverova,
byt 0001,45 m2,Olomouc,ul.Zirmova,
byt 0006,114 m2,Olomouc,ul.Přichystalová,
'''

l = DATA_SCRAP.splitlines()[1:] #nebo split("\n")
#nebo DATA_SCRAP.strip().splitlines()
newl = []

for j in l:
    newl.append(j.split(",")[:-1])

# P2
# Definujeme vzor, jak chceme data prevest
# Vzor prevadeni:
#1 - 1+1
#2 - 2+1
#3 - 2+kk
#4 - 3+1
#5 - 3+kk
#6 - 4+1
#7 - 4+kk

plus = ["", "1+1", "2+1", "2+kk", "3+1", "3+kk", "4+1", "4+kk"]
newnewl = []
nova_pol = []
for k in newl:
    a, *b = k
    if a == "byt 0001" :  a = plus[1]
    elif a == "byt 0002" : a = plus[2]
    elif a == "byt 0003" : a = plus[3]
    elif a == "byt 0004" : a = plus[4]
    elif a == "byt 0005" : a = plus[5]
    elif a == "byt 0006" : a = plus[6]
    elif a == "byt 0007" : a = plus[7]
    nova_pol = [a, *b]
    print(nova_pol)
    newnewl.append(nova_pol)

print(newnewl)

#jeho:
""""
d_nahrada = {
            "byt 0001": "1+1",
            "byt 0002": "2+1",
            "byt 0003": "2+kk",
            "byt 0004": "3+1",
            "byt 0005": "3+kk",
            "byt 0006": "4+1",
            "byt 0007": "4+kk",
            }

# P4
# Potrebujeme rozdelit jednotlive atributy
# Idealne na typ, plocha, mesto, ulice
for polozka in new_data:
    typ, *zbytek = polozka
    novy_typ = d_nahrada[typ] #  -->'1+1'
    novy_seznam = [novy_typ, *zbytek]
    print(novy_seznam)
"""
# funkce v Pythonu https://docs.python.org/3/library/functions.html#print
