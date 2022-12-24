# Funções aumentar(), diminuir(), dobro() e metade().
def aumentar(p=0, t=0, formatar=False):
    """
    Função para aumentar o preço conforme taxa
    :param p: indica o preço.
    :param t: indica a taxa.
    :param formatar: indica se será formatado ou não.
    :return: retorna o resultado
    """
    res = p + (p * t / 100)
    return res if formatar is False else moeda(res)


def diminuir(p=0, t=0, formatar=False):
    """
    Função para calcular a redução conforme uma taxa
    :param p: indica o preço.
    :param t: indica a taxa.
    :param formatar: define se será formatado ou não.
    :return: returna o resultado.
    """
    res = p - (p * t / 100)
    return res if formatar is False else moeda(res)


def dobro(p=0, formatar=False):
    res = p*2
    return res if formatar is False else moeda(res)


def metade(p=0, formatar=False):
    res = p/2
    return res if formatar is False else moeda(res)


def moeda(p=0, moeda='R$'):
    res = f'{moeda} {p:.2f}'.replace('.', ',')
    return res


def resumo(p=0, ta=10, td=5):
    print('-'*30)
    print('     RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{ta}% de aumento: \t{aumentar(p, ta, True)}')
    print(f'{td}% de redução: \t{diminuir(p, td, True)}')
    print('-' * 30)
