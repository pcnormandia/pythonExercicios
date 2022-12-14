sexo = str(input('Informe o sexo (M/F):')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, Informe o sexo (M/F): ')).upper().strip()[0]

print('Sexo {}. Registrado com sucesso'.format(sexo))
