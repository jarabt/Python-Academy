<<<<<<< HEAD
>>> sequence = [32,43,54,54,76,21,62,83,52,58]
>>> my_sum(sequence)
535
=======
import random

dataset= [['Name','Item','Amount','Unit_Price']]

customers = ['Bettison, Elnora',
             'Doro, Jeffrey',
             'Idalia, Craig',
             'Conyard, Phil',
             'Skupinski, Wilbert',
             'McShee, Glenn',
             'Pate, Ashley',
             'Woodison, Annie']
products = [('DROXIA', 33.86),('WRINKLESS PLUS',23.55),
            ('Claravis', 9.85), ('Nadolol', 12.35),
            ('Quinapril', 34.89), ('Doxycycline Hyclate', 23.43),
            ('Metolazone', 43.06), ('PAXIL', 14.78)]


row = [None]*5

for i in range(5):
    row[0] = random.choice(customers)
    row[1], row[3]= random.choice(products)
    row[2] = random.randint(1,100)
    row[4] = row[2] * row[3]
    dataset.append(row)


print(dataset)
>>>>>>> 2f08ea1fa793d367e766a611eceb2b9e53bbd0bc
