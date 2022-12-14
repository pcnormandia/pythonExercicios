# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
ind = list()
maiorp = menorp = 0
while True:
    ind.append(str(input('Nome: ')))
    ind.append(float(input(('Peso: '))))
    if len(pessoas) == 0:
        maiorp = menorp = ind[1]
    else:
        if ind[1] > maiorp:
            maiorp = ind[1]
        if ind[1] < menorp:
            menorp = ind[1]
    pessoas.append(ind[:])
    ind.clear()
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Deseja continuar [S/N: ')).upper().strip()[0]
    if resp == 'N':
        break

print('-=-'*10)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi {maiorp} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorp:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menorp} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorp:
        print(f'[{p[0]}] ', end='')
print()
