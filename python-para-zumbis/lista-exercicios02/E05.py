'''
Exercício 05 - Python para Zumbis
-------------
Faça um Programa que leia três números e mostre o maior e o menor deles. 
'''
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'Maior e menor número entre [{n1}, {n2}, {n3}]:\nMaior\t->\t{maior};\nMenor\t->\t{menor};')
