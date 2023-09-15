# listComprehension

valores = []

for x in range(6):
    valores.append(x * 10)


print(valores)

# reduzindo para 1 linha
valores2 = [x * 10 for x in range(6)]
print(valores2)