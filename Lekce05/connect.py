inputS = "The Czech Republic also known as Czechia, is a nation state in\
 Central Europe bordered by Germany to the west, Austria to the south, Slovakia\
 to the east and Poland to the northeast.[12] The Czech Republic covers an area\
 of 78,866 square kilometres (30,450 sq mi) with mostly temperate continental\
 climate and oceanic climate. It is a unitary parliamentary republic, has 10.5\
 million inhabitants and the capital and largest city is Prague, with over 1.2\
 million residents. The Czech Republic includes the historical territories of\
 Bohemia, Moravia, and Czech Silesia."

listInputS = inputS.split()
listInputSLens = []
listInputSBL = []
result = []

for word in listInputS:
    listInputSLens.append(len(word))
    listInputSBL.append(word[0])

for len in listInputSLens:
    if not listInputSBL:
        break
    newW = ""
    for n in range(len):
        newW += listInputSBL[0]
        listInputSBL = listInputSBL[1:]
        if not listInputSBL:
            break
    result.append(newW)

result = " ".join(result)

print(result)

"""
#jejich:
words = my_str.split()
inits = []
lengths = []

for w in words:
    # 1.
    lengths.append(len(w))
    # 2.
    inits.append(w[0])

result_string = ''

while inits:
    # 3.
    l = lengths.pop(0)
    # 4.
    if l >= len(inits):
        result_string = result_string + ''.join(inits)
        inits.clear()
    # 5.
    else:
        result_string = result_string + ''.join(inits[:l]) + ' '
        del inits[:l]
"""
