PREDMETY = ['Premenovani', 'Astronomie', 'Obrana_proti_cerne_magii',
            'Bylinkarstvi', 'Lektvary']

tridy = { }

SKUP_1 = ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann',
          'Ron', 'Hermiona']
SKUP_2 = ['Marcus','Alex','Glenn','Samuel', 'Hermiona', 'Clara','Chelsea']
SKUP_3 = ['Hermiona', 'Adam','Tyler', 'Alex','Clara']
SKUP_4 = ['Abraham','Marcus', 'Hermiona', 'Alex','Glenn','Clara']
SKUP_5 = ['Alfred', 'Curt','Oliver','Alex','Tyler', 'Hermiona', 'Ann']



tridy.update(Premenovani=SKUP_1)
tridy.update(Astronomie=SKUP_2)
tridy.update(Obrana_proti_cerne_magii=SKUP_3)
tridy.update(Bylinkarstvi=SKUP_4)
tridy.update(Lektvary=SKUP_5)

#print(tridy.keys())

set_premenovani = set(tridy["Premenovani"])
set_astronomie = set(tridy["Astronomie"])
set_obrana = set(tridy["Obrana_proti_cerne_magii"])
set_bylinkarstvi = set(tridy["Bylinkarstvi"])

print('Student(i), ktery(i) je/jsou vsude:', set_obrana & set_astronomie & \
set_premenovani & set_bylinkarstvi)
