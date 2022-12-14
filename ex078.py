valores = list()
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a {i}ª posição: ')))
    if i == 0:
        vMaior = vMenor = valores[i]
    else:
        if valores[i] > vMaior:
            vMaior = valores[i]
        if valores[i] < vMenor:
            vMenor = valores[i]

print(f'O maior valor é {vMaior} e está na posição: ', end='')
for p, v in enumerate(valores):
    if v == vMaior:
        print(f'{p}', end='..')
print()

print(f'O menor valor é {vMenor} e está na posição: ', end='')
for p, v in enumerate(valores):
    if v == vMenor:
        print(f'{p}', end='..')
print()
