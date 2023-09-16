quadrado = lambda num: num ** 2

num = int(input('Informe um número: '))
print(f'O quadrado de {num} é {quadrado(num)}')


lista=[]
for i in range(1, 11):
    lista.append(i)


lista2=[]
for item in lista:
    lista2.append(quadrado(item))


print(f'Os quadrados dos números {lista} é {lista2}')