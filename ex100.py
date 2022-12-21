# Exercício Python 100: faça um programa que tenha uma lista chamada números
# e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a
# segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
lista = []


def sorteia():
    for i in range(0, 5):
        lista.append(randint(0, 10))
    print(f'Para os números {lista}')


def somapar(num):
    soma = 0
    for valor in num:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares é: {soma}')


# Programa principal
sorteia()
somapar(lista)
