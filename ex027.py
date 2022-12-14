nome = str(input('Digite o nome completo: ')).strip().title()
lista = nome.split()
print('O primeiro nome é {}'.format(lista[0]))
print('O ultimo nome é {}'.format(lista[len(lista)-1]))
