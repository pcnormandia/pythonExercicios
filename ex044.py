print('{:=^60}'.format(' NORMANDIA STORE '))
valor = float(input('Qual o valor total das compras R$: '))
pagar = float(input('''Qual a forma de pagamento. Digite:
[ 1 ] Pagamento à vista (dinheiro ou cheque)
[ 2 ] Pagamento à vista no cartão
[ 3 ] Pagamento à prazo 2X no cartão
[ 4 ] Pagamento à prazo 3X ou mais no cartão:
Qual é a opção: '''))

if pagar == 1:
    print('Você teve um desconto de 10% e o preço final é R$ {:.2f}'.format(valor-(valor*10/100)))
elif pagar == 2:
    print('Você teve um desconto de 5% e o preço final é R$ {:.2f}'.format(valor-(valor*5/100)))
elif pagar == 3:
    print('Você irá pagar 2X parcelas de R${:.2f}.'.format(valor/2))
    print('Você não teve desconto o preço final é R$ {:.2f}'.format(valor))
elif pagar == 4:
    parcela = int(input('Em quantas parcelas deseja pagar:'))
    novoValor = valor + (valor * 20 / 100)
    prest = novoValor/parcela
    print('Sua compra será parcelada em {}X de {:.2f} com juros'.format(parcela, prest))
    print('Sua compra de R${:.2f} terá custo final de R${:.2f}'.format(valor, novoValor))
else:
    print('Opção invalida. Tente novamente')
