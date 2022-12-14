from random import randint
comp = randint(0, 10)
tent = 1
print('''Aqui é o seu computador. 
Pensei em um número entre 0 e 10''')
jog = int(input('Adivinhe qual número eu pensei: '))
while comp != jog:
    if jog > comp:
        jog = int(input('Menos. Tente novamente: '))
    else:
        jog = int(input('Mais. Tente novamente: '))
    tent += 1
print('Parabéns você acertou. Você precisou de {} tentativas'.format(tent))
print('Eu pensei no {}.'.format(comp))
