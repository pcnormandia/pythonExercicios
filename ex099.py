# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    pos = 0
    nmaior = 0

    while pos <= len(num):
        if pos == 0:
            nmaior = num[0]
        elif num[pos] > nmaior:
            nmaior = num[pos]
    print('-=-'*10)


valores = [2, 5, 10, 0]
maior(valores)
