'''
Exercício 03 - Python para Zumbis
-------------
Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.
'''
import random

lista1 = random.sample(range(1, 101), 10)  # 100 só entra com range de 101
lista2 = random.sample(range(1, 101), 10)
lista3 = []

for i in zip(lista1, lista2):
    lista3.extend(list(i))

print(f'lista 01: {lista1}\nlista 02: {lista2}\njunção: {lista3}\n')
