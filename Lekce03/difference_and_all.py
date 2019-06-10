String01 = 'Bratislava'
String02 = 'Budapest'

setStr1 = set(String01)
setStr2 = set(String02)

diff = setStr1.symmetric_difference(setStr2)
all = setStr1.union(setStr2)

print('Different characters:', diff)
print('All characters:', all)
