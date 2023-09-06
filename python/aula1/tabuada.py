numero = input("Informe um número de 1 a 10");

if (numero<=0 or numero > 10):

    print("Número incorreto, o programa será finalizado");
else:
    for(int i = 1; i < 11; i++):
        calculo = numero * i;
        calculo = str(calculo);

        print( str(numero) + " X " + str(i) + " = " calculo );
    