# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = list()

while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    resp = ' '
    while resp not in "NS":
        resp = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if resp == 'N':
        break
cont5 = 0



print('-=-'*10)
print(f'Foram digitados {len(valores)} valores.')
valores.sort(reverse=True)
print(f'Os valores ordenados em forma descrescente são:', valores )
if 5 in valores:
    print(f'O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
