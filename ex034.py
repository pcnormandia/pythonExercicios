sal = float(input('Qual é o salário do funcionário: R$ '))
if sal <= 1250:
    novoSal = sal + (sal*15/100)
else:
    novoSal = sal + (sal*10/100)
print('O novo salário do funcionário é R$ {:.2f}'.format(novoSal))
