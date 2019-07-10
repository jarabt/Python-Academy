anInput = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]
result = {}

for item in anInput:
    result.setdefault(str(item), 0)
    result[str(item)] += 1

ordered_data = sorted(result, key=result.get, reverse=True)

print(ordered_data)
