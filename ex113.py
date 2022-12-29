# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mPor favor digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados foi interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor favor digite um número real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados foi interrompida pelo usuário\033[m')
            return 0
        else:
            return f


print('-'*40)
n = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n} e o número real foi {f}')
