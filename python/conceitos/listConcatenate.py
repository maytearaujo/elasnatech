# Listas
    # Armazena mais de uma informação em variáveis
    # Manter a sequeência dos dados em uma variável

numeros = [2, 3, 4, 5]

# imprime a lista 2 vezes
final = numeros * 2
print(final)

# concatena listas
letras = ['a', 'b', 'c', 'd']
final = numeros + letras
print(final)

# extende letras em numeros
numeros.extend(letras)
print(numeros)

# lista dentro de listas (Array bidimensional)
itens = ['item1', 'item2', 'item3', 'item4']
print(itens)

itens2 = [['item1', 'item2'], ['item3', 'item4']]
print(itens2[1])    # ['item3', 'item4']
print(itens2[0][1]) # [item2]
