def reversed(seq):
    result = []
    while seq:
        result.append(seq[-1])
        seq = seq[:-1]
    return result

print(reversed(range(10)))


"""
# NOTE: jejich:
def my_reversed(sequence):

    return list(sequence[::-1])

# NOTE: nebo jejich:

def my_reversed(sequence):

    result = []

    for item in sequence:

        result.insert(0,item)

    return result
"""
