'''
Exercício 01 - Python para Zumbis
-------------
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, 
sem usar as funções max, min e sort. 
'''
import random

lista = []
lista = random.sample(range(1, 101), 10)  # 100 só entra com range de 101
mx = mn = lista[0]

for x in lista:
    if x > mx:
        mx = x
    if x < mn:
        mn = x

print(f'{lista}\nMax: {mx}\nMin: {mn}')
