import datetime

ano = datetime.date.today().year
nasc = int(input('Qual o ano de nascimento do atleta: '))
idade = ano - nasc
print('A idade do atleta é {} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM')
elif 14 >= idade > 9:
    print('Sua categoria é INFANTIL')
elif 19 >= idade > 14:
    print('Sua categoria é JUNIOR')
elif 25 >= idade > 19:
    print('Sua categoria é SENIOR')
elif idade > 25:
    print('Sua categoria é MASTER')
