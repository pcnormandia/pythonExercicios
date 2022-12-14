lista = []

while True:
    n = int(input('Digite um valor:'))
    if n in lista:
        print('Valor já digitado. Tente novamente!')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso!')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

    if resp == 'N':
        break

print(f'Você digitou os valores {sorted(lista)}')

