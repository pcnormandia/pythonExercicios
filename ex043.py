print('-=-'*20)
print('ANÁLISE DE INDICE DE MASSA CORPORAL - IMC')
print('-=-'*20)
peso = float(input('Qual o seu peso em Kg: '))
alt = float(input('Qual a sua altura em metros: '))
imc = peso/(alt**2)
print('Para o peso de {:.1f} Kg, e altura de {:.2f} metros, o seu IMC é de {:.1f}.'.format(peso, alt, imc))

if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif 25 > imc >= 18.5:
    print('Você está com o peso ideal')
elif 30 > imc >= 25:
    print('Você está com sobrepeso')
elif 40 > imc >= 30:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')
print('-=-'*20)
