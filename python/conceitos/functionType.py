# Function (Funções)
# Dry - Dont Repeat Your Self
# Realizam uma tarefa
# Calcula e retorna um valor

# Função 1 --> NÃO RETORNA VALOR
def cliente1(nome):
    print(f'Olá {nome}!')


# Função 2 --> RETORNA VALOR
def cliente2(nome):
    return(f'Olá {nome}!')


x = cliente1('Maria')
y = (cliente2('Jose'))

print(x)
print(y)