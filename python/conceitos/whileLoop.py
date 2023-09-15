# == While Loopd ==
# excelente para loops dependentes de uma condição

# criar uma promoção no valor de R$ 100 que vai reduzinhdo R$ 5a cada dia

valor = 100
dia = 1

while valor > 20:
    print(f' No dia {dia} o produto será vendido por R$ {valor}')
    dia += 1
    valor -= 5
