def potencia(base, expoente=2):
    result = base ** expoente
    return result


base = int(input('Informe a base: '))
expoente = input('Informe o expoente: ')

if expoente:
    print(f'O resultado é: {potencia(base, int(expoente))}') 
else:
    print(f'O resultado é: {potencia(base)}') 