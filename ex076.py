lista = (str(input('Produto: ')), float(input('Preço (R$): ')),
         str(input('Produto: ')), float(input('Preço (R$): ')),
         str(input('Produto: ')), float(input('Preço (R$): ')))
print('-=-'*15)
print('{:-^40}'.format(' Lista de preços '))
print('-=-'*15)

for c in range(0, 5):
    if c % 2 == 0:
        print('{:.<25}'.format(lista[c]), end=' ')
        print('{:<3}{:>5.2f}\n'.format('R$', lista[c+1]))
print('-=-'*15)
