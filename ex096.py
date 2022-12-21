# Função para cálculo da área
def area(a, b):
    c = a * b
    print(f'A área de um terreno de {a}m por {b}m é {c}m2')
    print('-=-'*15)


# Programa principal
print('Controle de terrenos')
print('-=-'*15)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l, c)

