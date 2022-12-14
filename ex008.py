m = float(input('Digite o valor em metros: '))
print('{:.2f} metros equivale a:\n{:.2f} dm\n{:.2f} cm\n{:.2f} mm'.format(m, (m*10), (m*100), (m*1000)))
print('{:.4f} km.\n{:.3f} hm\n{:.2f} dam'.format((m/1000), (m/100), (m/10)))
