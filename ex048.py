s = 0
cont = 0
for c in range(1, 501):
    if c%2 == 1:
        if c%3 == 0:
            s += c
            cont += 1
print('A somatória dos {} números impares e multiplos de três é {}.'.format(cont, s))
