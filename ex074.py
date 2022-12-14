from random import sample

# Substituido pelo método tuple
'''from random import randint
listax = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))'''

lista = tuple(sample(range(10), 5))
print(f'Os números sorteados foram: {lista}')

# Substituido pelo método max e min que pode ser usados para tuplas
'''for c in range(0, 5):
    if c == 0:
        menor = lista[0]
        maior = lista[0]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]'''

print(f'O menor valor é {min(lista)}')
print(f'O maior valor é {max(lista)}')
