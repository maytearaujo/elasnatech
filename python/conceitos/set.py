# Set (Listas)
    # Similar a listas
    # Evita itens duplicados
    # não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1)
print(num2)

# faz a união entre as list num1 e num2 e remove valores repetidos
print(num1 | num2) # | Union

# Mostra apenas valores únicos (que não se repetem)
print(num1 - num2) # - Diference

# remove todos os duplicados nas duas listas
print(num1 ^ num2) # - Symetric Diference

#Exibe os duplicados nas duas list
print(num1 & num2) # - And

print(len(num1)) # exibe o tamanho da list
