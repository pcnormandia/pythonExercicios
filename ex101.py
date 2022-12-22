# Exercício Python 101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


# Definição da função:
def voto(num):
    from datetime import date
    atual = date.today().year
    idade = atual - num
    if (16 <= idade < 18) or idade > 65:
        return f'Com {idade} anos o voto é FACULTATIVO'
    elif 18 <= idade < 65:
        return f'Com {idade} anos o voto é OBRIGATÓRIO'
    else:
        return f'Com {idade} anos NÃO VOTA'


# Programa principal:


nasc = int(input('Qual o ano de nascimento: '))
print(voto(nasc))
