# Desafio com funções

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuário deverá fornecer as seguintes informações: Rendimento, altura, largura.
O programa deve mostrar na tela a mensagem " Você necessita de x latas de tintas
'''

def quantidadeTinta(rendimento, altura, largura):
    return (altura * largura) / rendimento

rendimento = int(input('Informe o rendimento da tinta: '))
altura = int(input('Informe a altura da parede: '))
largura = int(input('Informe a largura da parede: '))

print(f'Você necessita de {quantidadeTinta(rendimento, altura, largura)} latas de tinta')