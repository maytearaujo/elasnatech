mensagem = 'Eu adoro COMIDA Caseira';
print(mensagem);            #mensagem original
print(mensagem.lower());    #minuscula
print(mensagem.upper());    #maiuscula
print(mensagem.capitalize())#primeira letra de cada palavra maiuscula
print(mensagem.find('o'));  #informa a posição da primeira letra o localizado
print(mensagem.find('adoro'));  #informa a posição da palavra adoro
#quando retorna -1 o valor não foi localizado
print(mensagem.replace('a', '@'));   #encontra o primeiro valor e troca pelo segundo
print(mensagem.replace('adoro', 'AMO'));   #encontra o primeiro valor e troca pelo segundo
print(mensagem.strip());    # remove espaços em branco no inicio da palavra
print(mensagem.isascii());

