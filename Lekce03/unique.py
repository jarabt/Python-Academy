str1 = 'New York'
str2 = 'Yorkshire'

print('Unique to str1', set(str1) - set(str2))
print('Unique to str2', set(str2) - set(str1))
