"""
    Print every element in the range 0 - 19
    Print every element in the range 15 - 19
    Print every third element in the range 10 - 19
    Create a list nums of every number divisible by 5 in range btw. 1 and 100
"""

print(list(range(20)))
print(list(range(15,20)))
print(list(range(10,20,3)))

nums = []

for number in range(1,101):
    if number%5 == 0:
        nums.append(number)

print(nums)

"""
# 4.

nums = list(range(5,101,5))

print(nums)
"""
