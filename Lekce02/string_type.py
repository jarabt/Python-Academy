s_input = input('Give me some input: ')
if s_input.isnumeric():
    print('Numeric')
elif s_input.isalpha():
    print('Only letters')
else:
    print('Mixed')
