from math import hypot, sqrt
n1 = float(input('Digite o comprimento do cateto adjacente do angulo: '))
n2 = float(input('Digite o comprimento do cateto oposto do angulo: '))
h = hypot(n1, n2)
print('O cumprimento da hipotenusa dos catetos {:.2f} e {:.2f} vale {:.2f}'.format(n1, n2, h))

'''Segundo método'''

hipo = sqrt((n1**2)+(n2**2))
print('O comprimento da hipotenusa dos catetos {:.2f} e {:.2f} vale {:.2f}'.format(n1, n2, hipo))

