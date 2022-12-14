a = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))
area = a*l
print('Sua parede tem {:.2f}m x {:.2f}m e uma área de {:.2f}m2'.format(a, l, (a*l)))
print('Para pintar esta parede você precisa de {:.2f} Litros de tinta'.format(area/2))
