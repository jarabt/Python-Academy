def min(items):
    min = items[0]
    for n in items[1:]:
        if n < min:
            min = n
    return min

def max(items):
    max = items[0]
    for n in items[1:]:
        if n > max:
            max = n
    return max

print(min([1, 0, 456]))
