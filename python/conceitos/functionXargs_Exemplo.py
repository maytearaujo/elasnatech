# Function (Funções)
    # Dry - Dont Repeat Your Self
    # Vários Argumentos (xargs)

# Criar uma função que armazena números e strings (dados).

def agencia(**carro):
    return carro


print(agencia(marca='Gol',  cor='Branco', motor=1.0, placa=1234))
print(agencia(marca='Gol',  cor='Azul', motor=1.0))
print(agencia(marca='Gol', cor='Preto'))