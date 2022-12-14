import random
from time import sleep
n1 = random.randint(1, 5)
print('-=-'*20)
n2 = int(input('Adivinha qual número eu escolhi de 1 a 5?'))
print('PROCESSANDO...')
sleep(2)
if n1 == n2:
    print('Você venceu miserável!!!')
else:
    print('Xiiii, você errou!!!')
print('Eu pensei no número {}'.format(n1))
print('-=-'*20)
