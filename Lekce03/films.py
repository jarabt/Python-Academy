from pprint import pprint as pp

'''
film = {}



film['Jmeno'] = ''
film['Hodnoceni'] = None
film['Rok'] = None
film['Reziser'] = None
film['Hraji'] = None

film['Jmeno'] = input('Zadej jmeno filmu: ')
film['Hodnoceni'] = 84
film.update(Hraji=['Robert Downwey Junior', 'Scarlet Johanson'])
film['Rozpocet'] = 200


'''
film2 = {
'Jmeno': 'The Godfather',
'Hodnoceni': 92,
'Rok': 1972,
'Reziser': 'Francis Ford Coppola',
'Hraji': ['Al Pacino', 'Marlon Brando']
}

film3 = {
'Jmeno':  'The Dark Knight',
'Hodnoceni': 90,
'Rok': 2008,
'Reziser': 'Christopher Nolan',
'Hraji': ['Christian Bale', 'Heath Ledger']
}

films = {film2['Jmeno']:film2, film3['Jmeno']:film3}

#films.update(Iron-man=film)

print('Máš tyto filmy: ', films.keys())
nazev = input('Zadej nazev filmu :')
print(films[nazev]['Hraji'])
