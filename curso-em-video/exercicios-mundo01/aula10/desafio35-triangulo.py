from cor import cores, estilos
print('{}{}Informe o tamanho de três retas...{}'.format(estilos['negrito'], cores['amarelo'], cores['limpa']))
a = int(input('Primeira reta: '))
b = int(input('Segunda reta: '))
c = int(input('Terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('{}Retas formam um triângulo!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}Retas NÃO formam um trângulo!{}'.format(cores['vermelho'], cores['limpa']))
