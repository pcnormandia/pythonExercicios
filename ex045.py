import random
from time import sleep
comp = random.randint(0, 2)
itens =('PEDRA', 'PAPEL', 'TESOURA')

print('{:=^40}'.format(' VAMOS JOGAR JOKENPÔ'))
opção = int(input('''Escolha uma das opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua opção: '''))

print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO')
print('-=-'*40)

print('O computador escolheu {} e você {}.'.format(itens[comp], itens[opção]))

if comp == 0:
    if opção == 0:
        print('EMPATE')
    elif opção == 1:
        print('JOGADOR VENCEU')
    elif opção == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('OPÇÃO INVALIDA')
elif comp == 1:
    if opção == 0:
        print('COMPUTADOR VENCEU')
    elif opção == 1:
        print('EMPATE')
    elif opção == 2:
        print('JOGADOR VENCEU')
    else:
        print('OPÇÃO INVALIDA')
elif comp == 2:
    if opção == 0:
        print('JOGADOR VENCEU')
    elif opção == 1:
        print('COMPUTADOR VENCEU')
    elif opção == 2:
        print('EMPATE')
