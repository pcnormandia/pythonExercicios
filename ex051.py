n = int(input('Digite o 1° termo: '))
razao = int(input('Digite a razão: '))
pa = n
print('Os 10 termos da progressão aritmética é:')
print(n, end='>')
for c in range(1, 10):
    pa += razao
    print(pa, end='>')
print('FIM')
