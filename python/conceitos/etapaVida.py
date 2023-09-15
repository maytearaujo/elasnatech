nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

idade = int(idade)

if idade <= 0:
    print(nome +" é recem nascido(a)")
elif idade > 0 and idade <= 11:
    print(nome +" é criança")
elif idade >= 12 and idade < 18:
    print(nome +" é adolescente")
elif idade >= 18 and idade < 60:
    print(nome +" é adulto")
else:
    print(nome +" é idoso")