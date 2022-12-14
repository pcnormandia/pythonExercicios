n = int(input('Digite o 1° termo:'))
r = int(input('Digite a razão:'))
pa = n
c = 1
print('Os primeiros 10 termos da razão aritmetica são:')
while c <= 10:
    print('{}>'.format(pa), end='')
    pa += r
    c += 1

print('FIM')
