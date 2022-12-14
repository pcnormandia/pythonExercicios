lista = (int(input('Digite o 1° valor: ')), int(input('Digite o 2° valor: ')),
         int(input('Digite o 3° valor: ')), int(input('Digite o 4° valor: ')))

print(f'Foram digitados os valores: {lista}')
print(f'O número 9 aparece {lista.count(9)} vezes')

if 3 in lista:
    print(f'O número 3 aparece na {lista.index(3) + 1}ª posição.')
else:
    print('A variável lista não possui o número 3')

print(f'Os números pares são:', end=' ')
par = 0
for c in lista:
    if c % 2 == 0:
        par += 1
        print(c, end=' ')
print(f'\nForam digitados {par} valores pares.')
