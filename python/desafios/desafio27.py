def fatorial(numero):
    i = 0
    i += 1

    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * fatorial(numero-1)
    

numero = int(input('Informe um número: '))
print(fatorial(numero))