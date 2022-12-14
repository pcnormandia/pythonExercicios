r = float(input('Quantos reais você tem? R$ '))
d = float(input('Qual a taxa de câmbio do dolar? '))
print('Então R$ {:.2f} equivalem a US$ {:.2f}'.format(r, (r/d)))
