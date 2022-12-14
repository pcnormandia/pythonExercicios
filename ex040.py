n1 = float(input('Digite a 1a nota: '))
n2 = float(input('Digite a 2a nota: '))
m = (n1 + n2) / 2

if m < 5.0:
    print('Sua média foi {:.1f}. Você foi reprovado.'.format(m))
elif m >= 5.0 and m <= 6.9:
    print('Sua média foi {:.1f}. Você está de recuperação.'.format(m))
else:
    print('Sua média foi {:.1f}. Parabéns você foi aprovado!'.format(m))
