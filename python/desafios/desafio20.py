# Criando a list
num = []
for n in range(1, 11):
    num.append(n)

# outra forma de criar a list
num = list(range(1, 11))
print(num)

for n in num:
    if n % 2 == 0:
        print(f'{n} é par')
    else:
        print(f'{n} é impar')
