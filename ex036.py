casa = float(input('Qual o valor do imóvel?: R$ '))
prazo = float(input('Qual o prazo de pagamento em anos: '))
sal = float(input('Qual o seu salário?: R$ '))

prest = casa/(prazo*12)
print('A prestação é estimada em R$ {:.2f}.'.format(prest))
limite = sal*30/100
print('O limite de 30% do seu salário de {:.2f} é R$ {:.2f}.'.format(sal, limite))
if prest <= limite:
    print('O valor da prestação é menor que o seu limite. Empréstimo pode ser concedido')
else:
    print('O valor da prestação é maior que o seu limite. Empréstimo negado')

print('O Banco Aenxo agradece sua consulta')
