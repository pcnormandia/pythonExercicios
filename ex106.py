# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’,
# o programa se encerrará. Importante: use cores.
from time import sleep
c = ('\033[m',         # 0 sem cores
     '\033[0;30;41m',  # 1 letra preta fundo vermelho
     '\033[0;30;42m',  # 2 letra preta fundo verde
     '\033[0;30;43m',  # 3 letra preta fundo amarelo
     '\033[0;30;44m',  # 4 letra preta fundo azul
     '\033[0;30;45m',  # 5 letra preta fundo roxo
     '\033[0;30;47m'   # 6 letra roxa fundo branco
    )


# Função para acessar os comandos utilizando o help e definindo o estilo de cor
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


# Função para personalizar o estilo do titulo
def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca > ')).lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)

