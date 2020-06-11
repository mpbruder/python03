'''
Exercício 02 - Python para Zumbis
-------------
Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. 
Imprima as três listas.
'''
import random

lista = []
par = []
impar = []

lista = random.sample(range(1, 101), 20)  # 100 só entra com range de 101

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'{lista}\n\nPares: {par}\nImpares: {impar}')
