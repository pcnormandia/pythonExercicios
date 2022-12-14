# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in "NS":
        resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

print('-=-'*12)
print('A lista dos valores digitados é:', valores)
valPar = []
valImpar = []
for c in valores:
    if (valores[c] % 2 == 0):
        valPar.append(valores[c])
    else:
        valImpar.append(valores[c])
print('A lista dos valores par é:', valPar)
print('A lista dos valores impares é:', valImpar)
