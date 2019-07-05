"""
Write a Python script that will calculate the sum of digits for every number in
the list: [1, 22, 321, 64221, 5657, 8321]. The result of this operation should
e stored in a new list and printed out to the terminal.

#moje:
givenList = [1, 22, 321, 64221, 5657, 8321]
result = []

for number in givenList:
    stringNList = list(str(number))
    sum = 0
    for digit in stringNList:
        sum += int(digit)
    result.append(sum)

print(result)
"""

#jejich:
lst = [1, 22, 321, 64221, 5657, 8321]
sums = []

# 1.
for num in lst:
    # 4.
    num_str = str(num)
    # 3.
    sums.append(0)

    # 2.
    for digit in num_str:
        # 3.
        sums[-1] = sums[-1] + int(digit)

print(sums)
