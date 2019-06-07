candidates = []
print('Candidates at the beginning: ' + str(candidates))
employees = ['Frank', 'Amy', 'John', 'Kate']
print('Employees at the beginning: ' + str(employees))
candidates += ['Bob', 'Ann']
print('Added new names to candidates: ' + str(candidates))
employees[1:1] = ['Bob']
print('Added new names to employees: ' + str(employees))
candidates.remove('Bob')
print('Removed name from candidates: ' + str(candidates))
candidates *= 3
print('Repeated name Ann in candidates: ' + str(candidates))
employees += candidates
print('Merged candidates with employees: ' + str(employees))
print('At index 2 we have: ' + employees[2])
print('At index ' + str(len(employees) - 1) + ' we have: ' + employees[-1])
print('At indices 2 to 5 we have: ' + str(employees[2:6]))
print('Every third member: ' + str(employees[::3]))
print('John is at index: ' + str(employees.index('John')))
print('The number of occurrences of Ann: ' + str(employees.count('Ann')))
