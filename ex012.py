pi = float(input('Digite o preço inicial: R$'))
d = float(input('Digite o percentual do desconto: '))
pf = pi-(pi*d/100)
print('O preço final é R$ {:.2f}'.format(pf))
