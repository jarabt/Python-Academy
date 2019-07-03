letter = input('Please enter a letter: ')
vowels = list('aeiouy')
if letter.isalpha() and len(letter)==1:
    print(letter in vowels)
