# Dicionários
    # Utiliza index no formato de keys e values
    # Aceita string, intege, float, boolean..

aluno = {'nome':'Ana', 'idade': 16, 'notaFinal': 'A', 'aprovação': True}

# Imprime as chaves
for x in aluno:
    print(x)
    
# Imprime os valores
for x in aluno.values():
    print(x)

# Imprime todas as informações, vem em formato de tuple
for x in aluno.items():
    print(x)

# Imprime todas as informações, sem estar dentro de tuple
for keys, values in aluno.items():
    print(keys, values)