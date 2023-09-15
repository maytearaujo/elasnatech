nome = input("Informe seu nome: ")
salario = input("Informe seu salário: ")
situacaoNome = input ("Você está com o nome limpo?: ")

salario = int(salario)

if(salario > 5000 and situacaoNome == 'true'):
    print(nome + " o financiamento foi aprovado")
else:
    print(" o financiamento foi reprovado")