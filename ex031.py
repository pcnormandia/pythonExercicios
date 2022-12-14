dist = int(input('Qual a distância em km: '))
if dist <= 200:
    print('A passagem custa R$ {:.2f}.'.format(dist*0.50))
else:
    print('A preço promocional da sua passagem custa R$ {:.2f}.'.format(dist*0.45))
