# Function (Funções)
#Dry - Dont Repeat Your Self

def boasVindas(nome, quantidade):

    print(f'Olá {nome}!')
    print(f'Temos {str(quantidade)} Laptops em estoque!')


nome = input('Informe seu nome: ')
quantidade = input('Informe a quantidade: ')

boasVindas(nome, quantidade)