numero = input("Informe um número de 1 a 10: ");
numero = int(numero)


def tabuada(numero):
    calculo = numero * i;
    calculo = str(calculo)
    return(f'{numero} X {i} = {calculo}' )


if (numero <= 0 or numero > 10):
    print("Número incorreto, o programa será finalizado");
else:
    for i in range(1,11) :
        print(tabuada(numero))