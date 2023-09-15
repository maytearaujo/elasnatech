#Multiple comparasion Operators (Multiplos Operadores de Comparação)
vlProduto = input("Informe o valor do produto: ")
vlProduto = int(vlProduto)

# if vlProduto >= 20 and vlProduto <= 40:
#     print("Produto liberado para cadastro")
# else:
#     print("Produto fora do valor")

# FORMA MENOS VERBOSA DE ESCREVER A MESMA CONDIÇÃO
if 20 <= vlProduto <= 40:
    print("Produto liberado para cadastro")
else:
    print("Produto fora do valor")