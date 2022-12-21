# Exercício Python 098: faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. Seu programa tem que realizar
# três contagens através da função criada:
# a) de 1 até 10, de 1 em 1.
# b) de 10 até 0, de 2 em 2.
# c) uma contagem personalizada.

# Definição da função contador
from time import sleep


def contador(i, f, p):
    cont = i
    if p == 0:
        p = 1
        cont -= p
    elif p > 0:
        cont -= p
    else:
        p = abs(p)
    print(f'Contagem de {i} a {f} em passos de {p} em {p}.')
    if i < f:
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(.5)
            cont += p
        print('FIM')
        print('-=-'*10)
    else:
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')
        print('-=-'*10)


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo:'))
contador(ini, fim, passo)
