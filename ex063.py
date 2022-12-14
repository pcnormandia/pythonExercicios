print('-=-'*10)
print('{:^20}'.format('Gerador de Sequencia Fibonacci'))
n = int(input('Quantos elementos você deseja:'))

menor = 0
maior = 1
fb = 0
c = 0

while c < n:
    c += 1
    print('{} > '.format(fb), end='')
    menor = maior
    maior = fb
    fb = menor + maior
print('FIM')
print('-=-'*10)
