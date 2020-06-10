'''
DESAFIO 01 - Python para Zumbis
-------------
Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. 
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular. 
'''
n = int(input('Digite número: '))
k = 1
while k * (k + 1) * (k + 2) < n:
    k += 1
print(k * (k + 1) * (k + 2) == n)
