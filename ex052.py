n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont += 1
        print('\033[31m', end='')
    else:
        print('\033[33m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} é divisivel {} vezes.'.format(n, cont))
if cont == 2:
    print('Por isso ele É primo.'.format(n, cont))
else:
    print('Por isso ele NÃO é primo.'.format(n, cont))


