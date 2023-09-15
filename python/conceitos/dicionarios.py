# Dicionários
    # Utiliza index no formato de keys e values
    # Aceita string, intege, float, boolean..

# Dicionário vazio
exemplo = {}

aluno = {'nome':'Ana', 'idade': 16, 'notaFinal': 'A', 'aprovação': True}

# lista completa
print(aluno)

# Permite exibir informações pelas keys
print(aluno['nome'])
print(aluno['idade'])

# Atualizar a chave nome
aluno['nome'] = 'José'
print(aluno)

# Permite Atualizar mais de um campo ao mesmo tempo
aluno.update({'nome': 'Josevaldo', 'notaFinal':'B'})
print(aluno)

# Atualiza a list incluindo o campo endereço 
aluno.update({'endereco':'Rua A'})
print(aluno)

print(aluno['nome'])

# Retorna um dado que não existe (erro)
#print(aluno['faltas'])

# Exibe uma mensagem caso o dado não exista
print(aluno.get('faltas', 'Informação inexistente'))

#remove dados
del aluno['idade']
print(aluno)