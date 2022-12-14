vel = float(input('Qual foi a velocidade registrada: '))
if vel > 80:
    print('Você ultrapassou a velocidade máxima de 80 km/h')
    print('A multa é de R$ {:.2f}'.format((vel-80)*7))

print('Tenha um bom dia. Dirija com segurança')
