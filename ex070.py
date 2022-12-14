print('-=-'*20)
print('{:-^40}'.format(' PAULO STORE '))
print('-=-'*20)
soma = c1000 = barato = c = 0
pBarato = ' '
while True:
    prod = str(input('Nome do Produto: ')).strip().upper()
    preço = float(input('Preço do produto:(R$) '))

    soma += preço
    c += 1
    if preço >= 1000:
        c1000 += 1
    if c == 1:
        barato = preço
        pBarato = prod
    else:
        if preço < barato:
            pBarato = prod
            barato = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(':-^40'.format(' FIM DO PROGRAMA '))
print(f'O total da compra é R${soma:.2f}')
print(f'{c1000} produtos custam mais de R$1000')
print(f'O produto mais barato foi {pBarato} que custa {barato:.2F}')
