cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

# LIST converte uma palavra em um array de char (caracteres)
var = list('comprar')
print(var)

var = list('Welcome')
print(var)

# zip (agrega duas listas mantendo o mesmo index)

duasListas = zip(cores, valores)
# o list é usado para converter para list novamente
print(list(duasListas))