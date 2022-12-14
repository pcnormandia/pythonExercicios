nome = str(input('Digite um nome completo: '))
print('O nome em maiusculas é {}'.format(nome.upper()))
print('O nome em minusculas é {}' .format(nome.lower()))
print('O nome com as primeiras letras maiusculas é {}'.format(nome.title()))
print('O total de letras do nome é: {}'.format(len(nome)-(nome.count(' '))))
pri = nome.split()
print('O 1° nome é {} e tem {} letras '.format(pri[0].upper(), len(pri[0])))

