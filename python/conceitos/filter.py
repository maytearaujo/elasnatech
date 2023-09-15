# Filter
    # Muito utilizado com listas
    # Aplicar uma função a um Iterable, filtrando os itens. (list, dic, tupple)

valores = [10, 12, 34, 44, 51]

def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))

# reduzindo para 1 linha
print(list(filter(lambda x: x > 20,valores)))