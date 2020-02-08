print('Informe sequencialmente três números inteiros')
x = int(input('Primeiro número: '))
y = int(input('Segundo número: '))
z = int(input('Terceiro número: '))
# Maior numero
maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z
# Menor numero
menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z

print('Maior é {} e menor é {}.'.format(higher, smaller))
