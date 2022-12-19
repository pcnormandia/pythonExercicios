# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Média do aluno: '))
sit = ''
if aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Aprovado'
print('-=-'*10)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
