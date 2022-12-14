import datetime
nasc = int(input('Digite o ano do seu nascimento: '))

ano = datetime.date.today().year
idade = ano - nasc

alist = ano - nasc
if alist < 18:
    print('Você ainda é muito novo para se alistar.')
    print('Você deve se apresentar no ano {} quando completa 18 anos.'.format(nasc+18))
elif alist == 18:
    print('Já está na hora de você se apresentar para o alistamento militar')
else:
    print('Você já passou {} anos da hora de se alistar.'.format(alist-18))
    print('Você deveria ter se apresentado em {}.'.format(nasc + 18))
