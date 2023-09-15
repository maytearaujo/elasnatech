# Dicionários
    # Utiliza index no formato de keys e values
    # Aceita string, intege, float, boolean..

aluno = {
    'nome':'Ana', 
    'idade': 16, 
    'notaFinal': 'A', 
    'aprovação': True, 
    'materias': ['fisica', 'matemática', 'Inglês']
}

print(aluno)
print(aluno.get('materias'))

# quantidade de chaves (keys)
print(len(aluno))

# imprime keys e valores
print(aluno.items())
print(aluno.keys())
print(aluno.values())