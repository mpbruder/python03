'''
Exercício 04 - Python para Zumbis
-------------
Faça um Programa que leia três números e mostre o maior deles. 
'''
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
m = n1
if n2 > m:
    m = n2
if n3 > m:
    m = n3
print(f'Maior número entre [{n1}, {n2}, {n3}]: {m}')
