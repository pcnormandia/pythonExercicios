# Exercício Python 103: faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa principal
print('-'*40)
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))

# Validação do número de gols
if g.isnumeric():
    g = int(g)
else:
    g = 0
# Validação do número do jogador
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)



