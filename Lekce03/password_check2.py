data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}
user = input('Please enter username: ')
passw = input('Please enter password: ')

if data.get(user) == passw:
    print('Permission continue, GRANTED!')
else:
    print('Password or username are WRONG!')
