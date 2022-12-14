frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

# técnica de fatiamento para inverter
# inverso = junto[::-1]

