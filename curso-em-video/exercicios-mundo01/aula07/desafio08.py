medida = int(input('Digite um valor em metros: '))
print('{:=^50}'.format(' TABELA DE CONVERSAO '))
print('Quilometro: {}km'.format(medida * 0.001))
print('Hectometro: {}hm'.format(medida * 0.01))
print('Decametro: {}dam'.format(medida * 0.1))
print('Metros: {}m'.format(medida))
print('Centimetros: {}cm'.format(medida * 100))
print('Milimetros: {}mm'.format(medida * 1000))