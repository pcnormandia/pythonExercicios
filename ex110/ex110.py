# Exercício Python 110: adicione o módulo moeda.py criado nos desafios anteriores,
# uma função chamada resumo(), que mostre na tela algumas informações geradas
# pelas funções que já temos no módulo criado até aqui.

import moeda

preco = float(input('Digite um preço: R$ '))
moeda.resumo(preco, 20, 12)

