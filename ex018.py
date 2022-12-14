from math import radians, sin, cos, tan
a = float(input('Digite um angulo em graus: '))
r = radians(a)
seno = sin(r)
cos = cos(r)
t = tan(r)
print('O angulo de {:.2f} graus tem {:.2f} graus radianos.\nO seno vale {:.2f}\nO cosseno {:.2f}'.format(a, r, seno, cos))
print('A tangente vale {:.2f}'.format(t))

