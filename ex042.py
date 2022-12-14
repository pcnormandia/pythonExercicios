a = float(input('Digite o valor do lado A em cm: '))
b = float(input('Digite o valor do lado B em cm: '))
c = float(input('Digite o valor do lado C em cm: '))

if a+b > c and a+c > b and c+b > a:
    print('Os lados são capazes de formar um triângulo')
    if a == b == c:
        print('Tipo EQUILATERO')
    elif a != b != c:
        print('Tipo ESCALENO')
    elif (a == b and b != c) or (b == c and c != a) or (a == c and c != b):
        print('Tipo ISÓCELES')
else:
    print('Não é possível formar um triângulo')

