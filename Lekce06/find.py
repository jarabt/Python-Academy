def find(seq, object):
    for index, item in enumerate(seq):
        if item == object:
            return index
    return -1


print(find("Nazdar", "p"))
