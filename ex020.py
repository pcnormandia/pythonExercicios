import random
a1 = input('Digite o nome do 1° aluno: ')
a2 = input('Digite o nome do 2° aluno: ')
a3 = input('Digite o nome do 3° aluno: ')
a4 = input('Digite o nome do 4° aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('A lista dos sorteados é {}'. format(lista))
