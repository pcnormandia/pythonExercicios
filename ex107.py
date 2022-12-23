# Exercício Python 107: crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from ex107 import moeda

preco = float(input('Digite um preço: R$ '))

print(f'A metade do preço é : R$ {moeda.metade(preco)}')
print(f'O dobro do preço é: R$ {moeda.dobro(preco)}')
print(f'Aumentando em 10% temos {moeda.aumentar(preco, 10)}')

