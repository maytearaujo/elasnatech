# Erros
    # Excelentes para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

letras = ['a', 'b', 'c']

try:
    print(letras[3])
except IndexError:
    print('Index não existe')

