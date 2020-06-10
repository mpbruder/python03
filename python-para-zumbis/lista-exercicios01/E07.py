'''
Exercício 07 - Python para Zumbis
-------------
Converta uma temperatura digitada em Celsius para Fahrenheit. (F = 9*C/5 + 32)
'''
print('CELSIUS para FAHRENHEIT')
print()
c = float(input('Digite a temperatura (ºC): '))
f = 9 * c / 5 + 32
print(f'{c:.2f}ºC == {f:.2f}ºF')
