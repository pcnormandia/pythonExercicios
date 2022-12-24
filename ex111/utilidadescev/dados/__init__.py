# Função para validação de valores monetários.

def leiadinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).replace(',', '.')
        if n.isnumeric():
            valor = float(n)
            ok = True
        else:
            print(f'Erro {n} é um preço invalido')
            ok = False
        if ok:
            break
    return valor



