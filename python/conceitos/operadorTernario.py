#  Ternary Operator (Operador Ternário)

idade = input('Informe sua idade: ')
idade = int(idade)

# if (idade >= 16):
#     resultado = print('Voto permitido')
# else:
#     resultado = print('Voto ainda não está liberado')
# print(resultado)

resultado = 'Voto Permitido' if idade >= 16 else "Voto não está permitido"

print(resultado)