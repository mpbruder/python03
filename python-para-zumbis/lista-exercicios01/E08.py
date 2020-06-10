'''
Exercício 08 - Python para Zumbis
-------------
Converta uma temperatura digitada em Fahrenheit para Celsius.
'''
print('FAHRENHEIT para CELSIUS')
print()
f = float(input('Digite a temperatura (ºF): '))
c = (f - 32) * 5 / 9
print(f'{f:.2f}ºF == {c:.2f}ºC')
