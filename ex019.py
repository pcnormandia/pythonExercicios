import random

a1 = str(input('Digite o nome do aluno 1: '))
a2 = str(input('Digite o nome do aluno 2: '))
a3 = str(input('Digite o nome do aluno 3: '))
a4 = str(input('Digite o nome do aluno 4: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

'''Segundo método de implementação: inclusão de vetor'''
print('O aluno escolhido foi {}'.format(random.choice([a1, a2, a3, a4])))
