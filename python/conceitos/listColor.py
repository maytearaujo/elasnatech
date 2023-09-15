cores = ['amarelo', 'verde', 'azul', 'vermelho']

corCliente = input('Informe a cor desejada: ')

if corCliente.lower() in cores:
    print('Em estoque')
else:
    print('Não temos está cor em estoque')