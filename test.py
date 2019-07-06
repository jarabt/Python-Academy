d = {'1': 4, '8': 1, '321': 1, '4': 1, '3': 2, '6': 2, '21': 1, '32': 1, '5': 2, '2': 3, '9': 1}


max = 0

while d:
    for key in d:
        if d[key] > max:
            max = d[key]
            keyMax = key
    del d[keyMax]

print(d)
