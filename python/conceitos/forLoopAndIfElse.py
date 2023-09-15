# For Loops (Looping)

compraConfirmada = True
dadosCompra = 'Compra no valor de R$ 12.50 e entrega confirmada'

for enviar in range(3):
    if compraConfirmada:
        print(dadosCompra)
        print('Detalhes enviados para seu e-mail')
        break
    else:
        print('Falha na compra')