# math.ceil() é usada para arredondamento para cima
# math.floor() é usada para arredondamento para baixo
# preciso usar a biblioteca -> "import math"

alt = float(input('Altura: '))
larg = float(input('Largura: '))
area = alt * larg
qnt_tinta = area/2
print('\nArea da parede: {:.3f}m²'.format(area))
print('Quantidade de tinta: {:.2f}L'.format(qnt_tinta))
