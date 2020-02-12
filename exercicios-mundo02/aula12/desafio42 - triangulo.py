from cor import cores, estilos
print('{}{}Informe o tamanho de três retas...{}'.format(estilos['negrito'], cores['amarelo'], cores['limpa']))
a = int(input('Primeira reta: '))
b = int(input('Segunda reta: '))
c = int(input('Terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        tipo = 'EQUILÁTERO'
    elif a != b and a != c and b != c:
        tipo = 'ESCALENO'
    else:
        tipo = 'ISÓCELES'
    print('{}Retas formam um triângulo {}!{}'.format(cores['verde'], tipo, cores['limpa']))
else:
    print('{}Retas NÃO formam um trângulo!{}'.format(cores['vermelho'], cores['limpa']))