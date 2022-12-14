frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra (a) aparece {} vezes'.format(frase.count('a')))
print('Primeira vez  na posição {}'.format(frase.find('a')+1))
print('Por ultimo na posição {}'. format(frase.rfind('a')+1))
