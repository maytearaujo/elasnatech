# Function (Funções)
#Dry - Dont Repeat Your Self
# Parametro --> Argumento
# Defaul = Aquele que você define o valor no parametro
# Non-Default = Aquele que você não define o valor no parametro
# REGRA: 1º DECLARA PARAMETROS NON-DEFAULt (irão mudar de valor) E DEPOIS OS PARAMETROS DEFAULT (Não mudam de valor)

def boasVindas(nome, quantidade=6):

    print(f'Olá {nome}!')
    print(f'Temos {str(quantidade)} Laptops em estoque')



nome = input('Informe seu nome: ')
# quantidade = input('Informe a quantidade: ')

boasVindas(nome)

#Sobrescrevendo argumento (quantidade) padrão
boasVindas(nome, 4)