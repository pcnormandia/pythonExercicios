from random import randint
print('-=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-'*20)
c = 0
while True:
    com = randint(0, 10)
    n = int(input('Diga um número (0 a 10): '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    soma = n + com
    parImpar = soma % 2
    print(f'Você jogou {n} e o computador {com}. Total é {soma}. ', end='')
    print('Deu par' if parImpar == 0 else 'Deu impar')

    if escolha == 'P':
        if parImpar == 0:
            print('VOCÊ GANHOU!!!')
            c += 1
        else:
            print('VOCÊ PERDEU!!!')
            break
    else:
        if parImpar == 0:
            print('VOCÊ PERDEU!!!')
            break
        else:
            print('VOCÊ GANHOU!!!')
            c += 1
    print('Vamos Jogar novamente')
    print('-=-'*20)
print(f'GAME OVER, Você venceu {c} vezes.')

