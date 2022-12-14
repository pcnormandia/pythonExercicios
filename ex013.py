sa = float(input('Digite seu salário atual: '))
au = float(input('Digite o percentual de aumento: '))
sf = sa+(sa*au/100)
print('Seu salário atual é R${:.2f} e com o aumento de {:.2f}% seu novo salário será R${:.2f}'.format(sa, au, sf))
