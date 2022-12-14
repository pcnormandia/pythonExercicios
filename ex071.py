print('{:-^40}'.format(' BANCO 24 HORAS '))
v = float(input('Valor do saque: R$'))

nota50 = v // 50
r50 = v % 50
nota20 = r50 // 20
r20 = r50 % 20
nota10 = r20 // 10
r10 = r20 % 10
nota01 = r10

print('-=-'*20)
print(f'Seu saque de R${v:.2f} será realizado em:')
if nota50 != 0:
    print(f'Total de {nota50} notas de R$ 50,00')
if nota20 != 0:
    print(f'Total de {nota20} notas de R$ 20,00')
if nota10 != 0:
    print(f'Total de {nota10} notas de R$ 10,00')
if nota01 != 0:
    print(f'Total de {nota01} notas de R$ 1,00')
print('O Banco Paulo Agradece. Tenha um bom dia')
print('-=-'*20)
