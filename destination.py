# Greet client
print('=' * 50)
print('Welcome to DESTINATION')

# Print our offer
print('''
We offer:

Destination                     Price
1 - Prague                      1000
2 - Wien                        1100
3 - Brno                        3000
4 - Svitavy                     1500
5 - Zlín                        2300
6 - Ostrava                     3400
''')
print('=' *50)

# Constants
DESTINATIONS = ['Prague', 'Wien', 'Brno', 'Svitavy', 'Zlín', 'Ostrava']
PRICES = [1000, 1100, 3000, 1500, 2300, 3400]
DISCOUNT_25 = ['Svitavy', 'Ostrava']

# Handling with destination
selection = int (input('Input the destination\'s number: '))
if selection >= len(DESTINATIONS) or selection <= 0:
    print('You did not enter a destination number in a correct range')
destination = DESTINATIONS[selection-1]
price = PRICES[selection-1]
if destination in DISCOUNT_25:
    print('Lucky you! You have just earned 25% discount for your destination - '\
    + destination)
    input('Press enter to continue')
    price *= .75

# Registration
print('''
REGISTRATION:
In order to complete your reservations, please share few details about yourself with us.
''')
name = input('FIRST NAME: ')
surname = input('SURNAME: ')
year = int(input('YEAR OF BIRTH: '))
email = input('EMAIL: ')
password = input('PASSWORD: ')

# Checking the registration
if year > 2004:
    print('We cannot provide our services to clients under 15 years of age')
elif not ('@' in email):
    print('Emails have to contain @ symbol')
elif len(password) < 7 or password[0].isnumeric() or password[-1].isnumeric() or \
password.isalpha() or password.isnumeric():
    print('Password has to be at least 8 chars long, cannot begin and end with a \
    number and has to contain both letters and numbers')

# Successful finish of the program
else:
    print('Thank you ' + name)
    print('We have made your reservation to ' + destination)
    print('The total price is ' + str(price))
