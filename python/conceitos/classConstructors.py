# criando a classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, dataNascimento):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.dataNascimento = dataNascimento
# criando o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')
usuario3 = Funcionarios('Andre', 'Iacono', '11/03/2003')


# Print
print(usuario1.nome)
print(usuario2.nome)
print(usuario3.sobrenome)

# imprimir nome e sobrenome ususario 1
print(usuario1.nome + ' ' + usuario1.sobrenome)

                                                                  