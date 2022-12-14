print('-=-'*20)
print('Conversor de bases numéricas')
print('-=-'*20)
n = int(input('Digite um número inteiro decimal: '))
tipo = int(input('Qual base numérica você deseja? 2 (binária), 8 (octal), 16 (hexidecimal): '))

if tipo == 2:
    print('O valor decimal {} em binário é {}.'.format(n, (format(n, 'b'))))
elif tipo == 8:
    print('O valor decimal {} em binário é {}.'.format(n, (format(n, 'o'))))
elif tipo == 16:
    print('O valor decimal {} em hexadecimal é {}.'.format(n, (format(n, 'X'))))
else:
    print('Opção invalida. Tente novamente')
print('-=-'*20)
