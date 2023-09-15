# set (Listas)
    # Similar a listas
    # Evita itens duplicados
# Não utiliza index

# transforma uma list em set
list1 = set([1, 2, 3, 5, 6])

# cria um set
s1 = {1, 2, 3, 5, 6}


print(s1)
print(list1)

print(type(list1))
print(type(s1))

# adiciona item
s1.add(7)
print(s1)

# adicionar mais de um item
s1.update([7, 8, 9, 10])
print(s1)

# remover - gera um erro se o item não existir
s1.remove(10)
print(s1)

# dicarta valores mas não gera erro caso o item não exista
s1.discard(9)
print(s1)