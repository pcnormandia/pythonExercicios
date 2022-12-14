# Exercício Python 086: crie um programa que declare uma matriz de dimensão 3×3 e
# preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

val = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for i in range(0, 3):
        val[c][i] = int(input(f'Digite um valor para [{c},{i}]: '))
for c in range(0, 3):
    for i in range(0,3):
        print(f'[{val[c][i]:^5}] ', end='')
    print()
