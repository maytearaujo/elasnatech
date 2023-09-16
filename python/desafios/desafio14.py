print('Loop com break')
for numero in range(1, 11):
    print(numero)
    if numero == 5:
        break


print('\nLoop com continue')
for numero in range(1, 11):
    if (numero == 5):
        continue
    print(numero)