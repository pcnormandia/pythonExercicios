cBras = ('Palmeiras', 'Internacional', 'Fluminense', 'Flamengo', 'Corinthians',
               'Athletico PR', 'Atletico MG', 'América MG', 'Góias', 'Botafogo',
               'Santos', 'Bragantino', 'São Paulo', 'Fortaleza', 'Ceará SC', 'Coritiba',
               'Avaí', 'Cuiabá', 'Atletico GO', 'Juventude')
print('{:=^50}'.format(' Campeonato Brasileiro '))
print(f'A classificação do Campeonato Brasileiro 2022 é:\n{cBras}')
print('-=-'*20)
print(f'Os cinco primeiros colocados são: \n{cBras[:5]}')
print('-=-'*20)
print(f'Os quatro últimos colocados são: \n{cBras[-4:]}')
print('-=-'*20)
print(f'Os times em ordem alfabética são: \n{sorted(cBras)}')
print('-=-'*20)
print(f'O Atletico MG está na {cBras.index("Atletico MG")+1}ª posição.')
