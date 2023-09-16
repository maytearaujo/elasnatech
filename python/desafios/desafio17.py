age = int(input('Informe a sua idade: '))

if age < 13:
    print('Você é uma criança')
elif age >= 13 and age <= 19:
    print('Você é um adolescente')
else:
    print('Você é um adulto')