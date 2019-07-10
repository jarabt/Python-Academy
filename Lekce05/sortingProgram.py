names = ['Michal', 'Pepa', 'Honza',
        'Pavel', 'Lukas', 'Matej',
        'Iva', 'Klara', 'Jana',
        'Honza', 'Vasek','Milan', 'Michal'
        ]
result = []

while names:
    minS = names[0]
    for name in names:
        if name < minS:
            minS = name        
    result.append(minS)
    names.remove(minS)

print(result)
