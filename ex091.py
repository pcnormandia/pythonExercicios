# Exercício Python 091: crie um programa onde 4 jogadores joguem um dado e
# tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = dict()
ranking = list()
for c in range(1, 5):
    jogo[f'jogador{c}'] = randint(1, 6)

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('-=-'*20)
print('  == Ranking dos jogadores ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for k, v in enumerate(ranking):
    print(f'   {k+1}o lugar: {v[0]} com {v[1]} pontos')
    sleep(1)
