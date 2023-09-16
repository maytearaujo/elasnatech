paisesCapitais = {
    'África do Sul': 'Pretória', 
    'Brasil': 'Brasilia', 
    'Angola': 'Luanda', 
    'Chile': 'Santiago', 
    'Cuba':'Havana',
    'Canada': 'Ottawa'
}

pais = input('Informe o nome de um pais: ')

if (pais in paisesCapitais ):
    print(f'A capital de {pais} é {paisesCapitais[pais]}')
else:
    print('Desculpe, o país não está na nossa relação')