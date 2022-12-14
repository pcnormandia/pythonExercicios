total18 = totalM = totalF20 = 0
while True:
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ')).strip().upper()[0]
    i = int(input('Idade: '))
    c = ' '
    print('=-='*10)
    while c not in 'SN':
        c = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if c == 'N':
        break
    if i >= 18:
        total18 += 1
    if s == 'M':
        totalM += 1
    if s == 'F' and i < 20:
        totalF20 += 1
print('-=-'*10)
print(f'Total de pessoas cadastradas com mais de 18 anos é {total18}')
print(f'Total de homens cadastrados foi {totalM}.')
print(f'Total de mulheres cadastradas com menos de 20 anos é {totalF20}')

