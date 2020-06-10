'''
Exercício 05 - Python para Zumbis
-------------
Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.  
'''
n1 = int(input('Número 01: '))
n2 = int(input('Número 02: '))
a, b = n1, n2
while a % b != 0:
    a, b = b, a % b
print(f'Máximo divisor comum entre [{n1}] e [{n2}]: {b}')
