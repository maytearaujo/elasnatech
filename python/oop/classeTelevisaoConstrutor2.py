class Televisao():
    # construtor (sempre usar self)
    def __init__(self, marca, ano, n_canais, preco):
        #print('O objeto {} foi construido'.format(self))
        self.marca = marca
        self.ano = ano
        self.n_canais = n_canais
        self.preco = preco


tv = Televisao('LG', 2023, 40, 1200)
print(tv.marca, tv.ano, tv.n_canais, tv.preco)

tv2 = Televisao('AOC', 2021, 80, 2000)
print(tv2.marca, tv2.ano, tv2.n_canais, tv2.preco)