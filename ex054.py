import datetime
atual = datetime.date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Qual o ano de nascimento da {}° pessoa: '.format(c)))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('No total temos {} menores de idades e {} maiores de idade.'.format(menor, maior))

