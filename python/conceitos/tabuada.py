numero = input("Informe um número de 1 a 10: ");
numero = int(numero)

if (numero <= 0 or numero > 10):

    print("Número incorreto, o programa será finalizado");
else:
    for i in range(1,11) :
        calculo = numero * i;
        calculo = str(calculo)
        print(f'{numero} X {i} = {calculo}' )