def dobro(numero):
    return numero * 2


def quadrado(numero2):
    return dobro(numero) ** 2



numero = int(input('Informe um número: '))
print(f'O dobro de {numero} é {dobro(numero)}')

print(f'O Quadrado do dobro de {numero} é {quadrado(numero)}')
