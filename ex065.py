soma = cont = m = 0
resp1 = ''
menor = maior = 0
while resp1 != 'N':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    m = soma/cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp1 = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
print('Foram digitados {} valores e a média é {:.2f}'.format(cont, m))
print('O menor valor é {} e o maior valor {}'.format(menor, maior))
print('Fim do programa')
