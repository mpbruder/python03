'''
DESAFIO 04 - Python para Zumbis
-------------
Dado um número inteiro positivo, determine a sua decomposição em fatores primos calculando também a multiplicidade de cada fator. 
'''
n = int(input('Número: '))
for i in range(2, n):
    while n % i == 0:
        print(f'{i}')
        n = n / i
