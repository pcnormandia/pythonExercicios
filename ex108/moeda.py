# Funções aumentar(), diminuir(), dobro() e metade().
def aumentar(p=0, t=0):
    res = p + (p * t / 100)
    return res


def diminuir(p=0, t=0):
    res = p - (p * t / 100)
    return res


def dobro(p=0):
    res = p*2
    return res


def metade(p=0):
    res = p/2
    return res


def moeda(p=0, moeda='R$'):
    res = f'{moeda} {p:.2f}'.replace('.', ',')
    return res

