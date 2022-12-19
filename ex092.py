# Exercício Python 092: crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também
# o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
atual = date.today().year

trab = dict()
trab['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
trab['idade'] = atual - ano
trab['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))

if trab['CTPS'] != 0:
    trab['contratação'] = int(input('Ano de contratação: '))
    trab['salario'] = float(input('Salário: R$ '))
    trab['aposentadoria'] = (trab['contratação'] + 35) - ano
print('-=-'*20)
for k, v in trab.items():
    print(f'    {k} tem o valor {v}.')
