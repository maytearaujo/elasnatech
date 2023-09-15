# set (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

# faz a união e remove duplicados
set4 = set1.union(set2)
print(set4)

# exibe apenas itens diferentes em ambas listas
set4 = set1.difference(set3)
print(set4)

# exibe apenas itens que são iguais em ambas listas
set4 = set1.intersection(set2)
print(set4)

# remove itens que são iguais em ambas
set4 = set1.symmetric_difference(set3)
print(set4)