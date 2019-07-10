

# http://www.pythontutor.com/visualize.html#mode=edit


converted_word = ''
for char in 'Python':
    if char.isupper():
        converted_word = converted_word + char.lower()
    else:
        converted_word = converted_word + char.upper()

print(converted_word)
