# Exercício Python 085: Crie um programa onde o usuário possa digitar
# sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]

for c in range(0, 7):
    n = int(input(f'Digite o {c+1}° valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
valores[0].sort()
print(f'Os valores pares são: {valores[0]}')
valores[1].sort()
print(f'Os valores impares são: {valores[1]}')

print(f'Os valores digitados foram: {valores}')
