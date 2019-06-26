students = ['Adam, Baker','Chelsea, Archer',
            'Marcus, Archer','Oliver, Cook',
            'Alex, Dyer', 'Sandra, Turner',
            'Ann, Fisher', 'Glenn, Hawkins',
            'Samuel, Baker','Clara, Slater',
            'Tyler, Hunt', 'Alex, Smith',
            'Clara, Woodman','Abraham, Mason',
            'Marcus, Sawyer','Alex, Glover',
            'Glenn, Cook','Clara, Fisher',
            'Alfred, Dyer', 'Curt, Head',
            'Oliver, Slater','Alex, Mason',
            'Tyler, Fisher','Ann, Parker',
            'Samuel, Hawkins', 'Ann, Woodman',
            'Sandra, Slater', 'Curt, Dyer']

firstnames = set()
surnames = set()


while students:
    #moje
    """
    name = students[0].split(", ")
    firstnames.add(name[0])
    surnames.add(name[1])
    students = students[1:]
    """
    #jejich
    name, surname = students.pop().split(', ')
    firstnames.add(name)
    surnames.add(surname)

print("Unique firstnames:", firstnames)
print("Unique surnames:", surnames)
