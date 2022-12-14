maiorP = 0
menorP = 0
maiorPes = 0
menorPes = 0
for c in range(1, 6):
    peso = float(input('Qual o peso da {}° pessoa: '.format(c)))
    if c == 1:
        maiorP = peso
        menorP = peso
        maiorPes = c
        menorPes = c
    else:
        if peso > maiorP:
            maiorP = peso
            maiorPes = c
        if peso < menorP:
            menorP = peso
            menorPes = c

print('O maior peso lido foi da {}° pessoa e foi de {} Kg'.format(maiorPes, maiorP))
print('O menor peso lido foi da {}° pessoa e foi de {} Kg'.format(menorPes, menorP))
