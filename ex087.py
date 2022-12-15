# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

val = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
col3 = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        val[l][c] = int(input(f'Digite um valor para a posição [{[l]},{c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        if (val[l][c]) % 2 == 0:
            par += val[l][c]
        if c == 2:
            col3 += val[l][c]
for l in range(1, 2):
    for c in range(0, 3):
        if c == 0:
            maior = val[l][c]
        if val[l][c] > maior:
            maior = val[l][c]
print('-=-'*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{val[l][c]:^5}] ', end='')
    print()
print('-=-'*15)
print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {col3}')
print(f'O maior valor da segunda linha é {maior}')
print('-=-'*15)
