print('-=-'*20)
print('Analisador de triangulos')
print('-=-'*20)
a = float(input('Digite o valor do 1° lado: '))
b = float(input('Digite o valor do 2° lado: '))
c = float(input('Digite o valor do 3° lado: '))
if a+b > c and a+c > b and c+b > a:
    print('Os segmentos de reta formam um triangulo')
else:
    print('Os segmentos de reta não formam um triângulo')

print('-=-'*20)