# function Lambda
    # é uma função (pequena) sem nome
    # pode ter vários argumentos mas somente uma expressão
    # Muito utilizada dentro de outras funções
    # Código mais 'clean'

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4


print(somar(2))