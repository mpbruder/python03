dist = float(input('Qual a distância da viagem? '))
print('A distância é {:.2f}Km, portanto:'.format(dist))
if dist > 200:
    valor = float(0.45)
else:
    valor = float(0.5)
print('Pague R${:.2f} pela passagem!'.format(dist * valor))
print('Tenha uma Boa Viagem!')
