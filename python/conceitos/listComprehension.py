# List Comprehension
    # Mais simples de se escrever
    # Utilizado quando você precisa criar uma nova lista a partir de uma existente
    # [Expressão for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kwi', 'abacaxi']
frutas2 = []

# verifica em fruta 1 quem contém a letra b e coloca em frutas2
for iten in frutas1:
    if 'b' in iten:
        frutas2.append(iten)


print(frutas2)

# verifica em fruta 1 quem contém a letra n e coloca em frutas2
# ======== reduzindo para uma linha
frutas2 = [iten for iten in frutas1 if 'n' in iten]

print(frutas2)