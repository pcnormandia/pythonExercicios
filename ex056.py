soma = 0
maiorI = 0
totalI = 0

for c in range(1, 5):
    nome = str(input('Nome da {}ª pessoa: '.format(c))).capitalize()
    idade = int(input('Idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Sexo da {}ª pessoa [F] feminino ou [M] masculino: '.format(c))).upper()
    soma += idade
    print('-'*40)
    if c == 1 and sexo == 'M':
        maiorI = idade
        velho = nome

    if sexo == 'M' and idade > maiorI:
        maiorI = idade
        velho = nome

    if sexo == 'F' and idade < 20:
        totalI += 1

print('A média das idades lidas é {}.'.format(soma/4))
print('O nome do homem mais velho é {}.'.format(velho))
print('O total de mulheres com menos de 20 anos é {}'.format(totalI))
