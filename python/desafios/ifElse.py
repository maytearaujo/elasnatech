# Desafio com If, Elif, Else

''' Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto de cozimento em portugues. O usuário deverá fornecer a temperatura 

Temperaturas - Cozimento
  0ºF ou  0ºC - Cozinhar por mais alguns minutos
120ºF ou 48ºC - Rare (Selada)
130ºF ou 54ºC - Medium rare (Ao ponto para o mal)
140ºF ou 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium well (Ao ponto para o bem)
160ºF ou 71ºC - Well done (Bem passada)
'''

temperatura = int(input("Informe a temperatura da carne: "))

if temperatura < 48:
    print('Cozinhar por mais alguns minutos')
elif temperatura >= 48 and temperatura <54:
    print('Selada')
elif temperatura >= 54 and temperatura < 60:
    print('Ao ponto para o mal')
elif temperatura >= 60 and temperatura < 65:
    print('Ao ponto')
elif temperatura >= 65 and temperatura < 71:
    print('Ao ponto para o bem')
else:
    print('Bem passada')


# VERSÃO DO PROFESSOR

'''if temperatura < 48:
    print('Cozinhar por mais alguns minutos')
elif temperatura in range(48, 53):
      print('Selada')
elif temperatura in range(54, 59):
    print('Ao ponto para o mal')
elif temperatura in range(60, 64):
    print('Ao ponto')
elif temperatura in range(65, 70):
    print('Ao ponto para o bem')
elif temperatura >=71:
    print('Bem passada')'''