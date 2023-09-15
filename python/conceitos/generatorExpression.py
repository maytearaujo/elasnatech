from sys import getsizeof

# Generator Expression
    # Uma forma mais rápida para listas, dicionários e etc
    # Menos memória alocada
    # Valores em bytes
    # Utiliza menos memória

numeros = [x * 10 for x in range(100000)]
print(type(numeros))
# print(numeros)
print(getsizeof(numeros))

print( '========' )
numeros = (x * 10 for x in range(100000))
print(type(numeros))
# print(list(numeros))
print(getsizeof(numeros))
