WEEKDAYS = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day_input = input('Please enter the number of the day (1-7): ')

if not day_input.isnumeric():
    print('Enter only numbers, please')
elif not day_input:
    print('No input provided')
else:
    n_day = int(day_input)
    print(WEEKDAYS[n_day-1])
