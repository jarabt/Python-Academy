String01 = 'Bratislava'
String02 = 'Budapest'

setStr1 = set(String01)
setStr2 = set(String02)

common = setStr1.intersection(setStr2)
unique = setStr1.difference(setStr2)

print('Common characters:', common)
print('Unique characters:', unique)
