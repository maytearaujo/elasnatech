# criando a classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, dataNascimento):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.dataNascimento = dataNascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    


# criando o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')
usuario3 = Funcionarios('Andre', 'Iacono', '11/03/2003')


# Print
print(usuario1.nome + ' ' + usuario1.sobrenome)
print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))


                                                                  