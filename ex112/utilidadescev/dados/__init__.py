# Função para validação de valores monetários.

def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31m Erro: \"{entrada}\" é um preço inválido\033[m')
        else:
            True
            return float(entrada)
