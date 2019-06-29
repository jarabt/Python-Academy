words = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']

max_length = 0

while words:
    a_word = words.pop()
    if len(a_word) > max_length:
        max_length = len(a_word)
        longest_word = a_word

result = longest_word, max_length
print(result)
