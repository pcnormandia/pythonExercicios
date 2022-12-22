# Exercício Python 102: crie um programa que tenha uma função fatorial()
# que receba dois parâmetros: o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional) indicando
# se será mostrado ou não na tela o processo de cálculo do fatorial.

# Definindo função
def fatorial(n, show=False):
    """
    =>Calcular o fatorial de um número
    :param n: número inteiro
    :param show: (opcional) apresentar ou não o cálculo
    :return: o valor do fatorial do número
    """
    fat = 1
    for c in range(n, 0, -1):
        fat *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
    return fat


# programa principal
num = int(input('Digite um número: '))
resp = str(input('Deseja mostrar o cálculo [S/N]: ')).upper().strip()[0]
if resp == 'S':
    r = True
else:
    r = False

print(fatorial(num, r))
print('-=-'*20)
help(fatorial)
