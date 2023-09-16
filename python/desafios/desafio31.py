parImpar = lambda num: 'Par'if num % 2 == 0 else 'Impar'

num = int(input('Informe um número: '))
print(f'{num} é {parImpar(num)}')