# Erros
    # Excelentes para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

# Exibe uma mensagem customizada ao encontrar um erro caso contrásrio realiza o cálculo
try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor válido')
else:
    print('Usuário digitou valor correto')
    resultado = valor * 2
    print(resultado)


print('Mais código a baixo')