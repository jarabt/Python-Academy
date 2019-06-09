# Database
my_db = {   'Name': 'John Smith',
            'Age': 34,
            'Address': {'Street': 'Main',
                'Street #': 241,
                'City': 'Boston',
                'Country': 'Venezuela'},

            'Job': {'Job Title': 'System Admin',
                    'Level' : 3}
}

my_db.update(Manager = 'Samuel, Hunt')

print(tuple(my_db.items()))
