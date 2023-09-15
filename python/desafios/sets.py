# Desafio com sets

'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

lista1 = funcionários que tem carro e trabalham a noite
lista2 = funcionários que tem carro e trabalham durante o dia
lista3 = funcionários que não tem carro
'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turnoDia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turnoNoite = ['Pedro', 'Sophia', 'Bruno']
temCarro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

setfuncionarios = set(funcionarios)
setturnoDia = set(turnoDia)
setturnoNoite = set(turnoNoite)
settemCarro = set(temCarro)

list1 = settemCarro & setturnoNoite
print(list1)

list2 = settemCarro & setturnoDia
print(list2)

list3 = setfuncionarios ^ settemCarro
print(list3)

'''
RESPOSTA DO PROFESSOR

lista1 = set(temCarro).intersection(turnoNoite)
print(lista1)

lista2 = set(temCarro).intersection(turnoDia)
print(lista2)

lista3 = set(funcionarios).difference(temCarro)
print(lista3)
'''