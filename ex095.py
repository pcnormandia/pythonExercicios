# Exercício Python 095: aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
time = list()
partidas = list()
tot = soma = 0

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na {c+1}a partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    partidas.clear()
    # Uso do método .append para adicionar os jogadores na lista time.
    time.append(jogador.copy())
    # Uso do laço while infinito para validar a resposta
    while True:
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro!!! Digite apenas S ou N')
    if resp == 'N':
        break
# Análise dos resultados
print('-=-'*15)
# Construção do cabeçalho da tabela usando as chaves do dicionário (.keys())
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
# Construção da tabela usando a propriedade enumerate da lista
# combinada com os valores do dicionário (.values())
for k, v in enumerate(time):
    print(f'{k:<3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=-'*15)

# Mostrar um jogador individualmente
while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador maior com código {busca}')
    else:
        print(f'---- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-=-'*15)
print('-=-'*15)
print('   <<< Volte sempre >>>   ')