'''
DESAFIO 03 - Python para Zumbis
-------------
Verifique se um inteiro positivo n é primo. 
'''
k = 0
for i in range(2, n):  # 2 até n-1
    if n % i == 0:
        k += 1
if k == 0:
    print(f'{n} é primo.')
else:
    print(f'{n} não é primo.')
