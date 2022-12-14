c = 0
while True:
    n = int(input('Você quer a tabuada de qual número [negativo para parar]: '))
    if n < 0:
        break
    print('-=-' * 5)
    print(f'TABUADA DE {n}')
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
        c +=1
    print('-=-'*5)
print('Fim do programa. Volte sempre')
