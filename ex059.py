from time import sleep
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número: '))
sair = False
soma = 0
mult = 1
maior = 0

while sair == False:
    print('-=-'*20)
    opção = int(input('''[1] Somar [2] Multiplicar [3] Maior Número [4] Novos números [5] Sair do programa
    Qual é a sua opção:'''))

    if opção == 1:
        soma = n1 + n2
        print('\033[031mA soma dos números {} e {} é {}\033[m'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('\033[032mO produto dos números {} e {} é {}\033[m'.format(n1, n2, mult))
    elif opção == 3:
        if n1 == n2:
            print('\033[033mOs números {} e {} são iguais\033[m'.format(n1, n2))
        else:
            if n1 > n2:
                print('\033[034mO número {} é maior que {}.\033[m'.format(n1, n2))
            else:
                print('\033[035mO número {} é menor que {}.\033[m'.format(n1, n2))
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(1)
        sair = True
    else:
        print('Opção invalida. Tente novamente')
    sleep(2)

print('='*40)
print('Fim do programa')