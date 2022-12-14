n = s = c = 0
n = int(input('Digite um valor [999 p/ parar]:'))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um valor [999 p/ parar]:'))
print('Foram digitados {} valores e a soma total é {}.'.format(c, s))
