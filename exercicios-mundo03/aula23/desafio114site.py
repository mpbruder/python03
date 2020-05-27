import urllib
import urllib.request
from cor import cores

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print(f'{cores["vermelho"]}O site não está acessível no momento.{cores["limpa"]}')
else:
    print(f'{cores["verde"]}O site foi acessado com sucesso.{cores["limpa"]}')
    print(site.read())