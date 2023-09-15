# function Lambda
    # é uma função (pequena) sem nome
    # pode ter vários argumentos mas somente uma expressão
    # Muito utilizada dentro de outras funções
    # Código mais 'clean'

# função original
def somar(x):
    return x + 10

print(somar(2))

# função lambda (muito utilizada dentro de outras funções)
somar10 = lambda x, y: x + y + 10

print(somar10(2, 4))
