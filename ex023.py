import random
n1 = random.randint(0, 9999)
u = n1//1%10
d = n1//10%10
c = n1//100%10
m = n1//1000%10
print('Analisando o número: {}'.format(n1))
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))
