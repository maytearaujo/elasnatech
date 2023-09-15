# Function (Funções)
    # Dry - Dont Repeat Your Self
    # Vários Argumentos (xargs)

# Criar uma função que soma vário valores.

def soma(*numeros):
    resultado = 0
    
    for num in numeros:
        resultado += num
    
    return resultado


x = soma(2, 3, 4, 7)
print(x)