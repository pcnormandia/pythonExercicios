print('-=-'*10)
print('{:^30}'.format('Gerador de Progressão aritmetica'))
print('-=-'*10)
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
t = int(input('Quantos termos você deseja: '))
print('-=-'*10)

resp = 1
pa = n
cont = 1
soma = t

while resp > 0:
    while cont <= t:
        print('{}>'.format(pa), end='')
        pa += r
        cont += 1
    print('')
    novoTermo = int(input('Quantos termos mais você deseja mostrar? '))
    n = pa
    resp = novoTermo
    t = novoTermo
    cont = 1
    soma += novoTermo

print('A PA foi apresentada com {} termos ao todo.'.format(soma))
