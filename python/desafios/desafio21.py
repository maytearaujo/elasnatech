citys = ('São Paulo', 'Rio de Janeiro', 'Salvador')

city = input('Informe o nome da cidade: ')

if city in citys:
    print(f'{city} está na lista de cidades')
else:
    print(f'{city} não está na lista de cidades')

print(type(citys))