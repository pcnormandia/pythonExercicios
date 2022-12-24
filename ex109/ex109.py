# Exercício Python 109: crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções

import moeda

preco = float(input('Digite um preço: R$ '))

print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando em 10% temos {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo em 13% temos {moeda.diminuir(preco, 13, True)}')
