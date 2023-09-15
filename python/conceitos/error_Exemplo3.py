# Erros
    # Excelentes para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

# Exibe uma mensagem customizada ao encontrar um erro e independente disso exibe codigo ok  
try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor válido')
finally:
    print('Código ok')