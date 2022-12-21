# Exercício Python 099: faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    nmaior = 0
    pos = 0
    print('\nAnalisando os valores passados...')
    while pos < len(num):
        if pos == 0:
            nmaior = num[pos]
        if num[pos] > nmaior:
            nmaior = num[pos]
        pos +=1

    print(f'{num}. Foram passados {len(num)} valores e o maior valor é: {nmaior}')
    print('-=-'*10)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
