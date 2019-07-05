"""
Write a Python program which prompts and accepts a string of comma-separated
numbers from a user and generates a list of those individual numeric strings
converted into numbers.
"""

stringFromUser = input("Please enter comma separated numbers: ")

l = stringFromUser.split(",")
result = []

for word in l:
    word = int(word.strip())
    result.append(word)

print(result)
