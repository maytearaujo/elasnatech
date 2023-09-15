# Map Function
    # Muito utulizado com listas
    # Aplicar uma função a um Iterable, por item. (list, tuple, dicionart, etc.)

# O exemplo multiplica o valor de lista1 por 2 e armazena em lista2
lista1 = [1, 2, 3, 4]

def mult(x):
    return x * 2


lista2 = map(mult, lista1)

print(list(lista2))


print(mult(2))