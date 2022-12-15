# Exercício Python 088: faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.


import random
from time import sleep
jogo = []
palpite = []
print('-=-'*20)
print('          Joga na Mega Sena')
print('-=-'*20)
jog = int(input('Quantos jogos você quer fazer: '))
cont = 0
for i in range(0, jog):
    while True:
        m = random.randint(1, 60)
        if m not in palpite:
            palpite.append(m)
            cont += 1
        if cont >= 6:
            break
    cont = 0
    palpite.sort()
    jogo.append(palpite[:])
    palpite.clear()
print('-=-'*20)
print('-=-'*2, f'Sorteando {jog} jogos', '-=-'*12)
for n in range(0, jog):
    print(f'Jogo {n+1}:', jogo[n])
    sleep(.7)
print('-=-'*20)
print('Boa sorte')
