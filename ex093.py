# Exercício Python 093: crie um programa que gerencie o
# aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

dados = dict()
gols = list()
soma = partida = 0
dados['nome'] = str(input('Nome do jogador: '))
partida = int(input(f'Quantas partidas {dados["nome"]} jogou?: '))
for c in range(0, partida):
    gols.append(int(input(f'   Quantos gols na {c+1}a partida: ')))
    soma += gols[c]
dados['gol'] = gols.copy()
dados['total'] = soma
print('-=-'*20)
for k, v in dados.items():
    print(f'   O campo {k} tem o valor {v}')
print('-=-'*20)
print(f'O jogador {dados["nome"]} jogou {partida} partidas.')
for k, v in enumerate(gols):
    print(f'   => Na {k+1}a partida, fez {v} gols.')
