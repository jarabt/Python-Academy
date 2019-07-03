list = [1,2,3]


def sum(collection):
    result = 0
    for number in collection:
        result += number
    return result

print(sum(list))
