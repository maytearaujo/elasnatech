from array import array

# Array
    # Similar as listas
    # melhor performance
    #utilizar quando preciso armazenar grande quantidade de itens (tem performance melhor que as listas)
    # precisa ser importado
    # é necessario atenção ao tipo de dados que será convertido

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)

print()

# Convertendo list em array
letras = array('u',  ['a', 'b', 'c', 'd'])
print(letras)

numeros_i = ('i', [10, 20, 30, 40])
print(numeros_i)

numeros_f = ('f', [1.2, 2.2, 3.2])
print(numeros_f)