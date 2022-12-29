# Exercício Python 114: crie um código em Python que teste
# se o site pudim está acessível pelo computador usado.

# Importação da biblioteca urllib
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Site não acessível.')
except:
    print('Houston, temos um problema')
else:
    print('Tudo ok. site acessível')
