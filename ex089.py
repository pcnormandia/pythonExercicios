# Exercício Python 089: Crie um programa que leia nome e duas notas
# de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []
aluno = []
m = 0
while True:
    aluno.append(str(input('Nome do aluno: ')))
    aluno.append(float(input('Nota 01: ')))
    aluno.append(float(input('Nota 02: ')))
    aluno.append((aluno[1] + aluno[2])/2)
    lista.append(aluno[:])
    aluno.clear()
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Deseja continuar [N/S]: ')).upper().strip()[0]
    if resp == 'N':
        break

print('-=-'*20)
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
print('-'*26)
for l, k, in enumerate(lista):
    print(f'{l:<4}{k[0]:<10}{k[3]:>8.1f}')
while True:
    print('-'*50)
    opc = int(input('Mostrar notas de qual aluno: '))
    print(f'Aluno: {lista[opc][0]}, nota 01: {lista[opc][1]} e nota 02: {lista[opc][2]}')
    resp = str(input('Deseja continuar [N/S]: '))
    if resp in 'Nn':
        break
