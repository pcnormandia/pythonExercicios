n = int(input('Escolha o número: '))
print('-=-'*10)
print('TABUADA DE {}'.format(n))
for c in range(1, 11):
    print('{:^2} X {:^2} = {:^2}'.format(n, c, n*c))
print('-=-'*10)
