# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

from datetime import date
atual = date.today().year

pessoas = dict()
lista = list()
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    while True:
        resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N')
    if resp == 'N':
        break

print('-=-'*20)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas')
media = soma/len(lista)
print(f'B) A média das idades é {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print('')
print(f'D) Lista das pessoas que estão acima da média: ', end='')
for p in lista:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<< ENCERRADO >>>>')
