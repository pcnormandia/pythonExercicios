# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
# a) Quantidade de notas
# b) A maior nota
# c) A menor nota
# d) A média da turma
# e) A situação (opcional)

def notas(*n, sit=False):
    """
    Função para analisar notas e situação de vários alunos.
    :param n: aceita uma ou várias notas de alunos.
    :param sit: (opcional) indica se deve ou não incluir a situação.
    :return: dicionário com várias informações sobre a situação da turma
    """

    maior = menor = media = p = s = 0
    tam = len(n)
    turma = dict()
    while p < tam:
        s += n[p]
        if p == 0:
            maior = n[p]
            menor = n[p]
        if n[p] > maior:
            maior = n[p]
        if n[p] < menor:
            menor = n[p]
        p += 1
    media = round(s/tam, 2)
    turma['total'] = tam
    turma['maior'] = maior
    turma['menor'] = menor
    turma['media'] = media
    if sit:
        if media < 5:
            turma['situação'] = 'ruim'
        elif 5 < media < 7:
            turma['situação'] = 'razoável'
        else:
            turma['situação'] = 'boa'

    return turma


# Programa principal
resp = notas(5.5, 2.5, 1.5, 10, 7.8, sit=True)
print(resp)
print('-=-'*15)
help(notas)
