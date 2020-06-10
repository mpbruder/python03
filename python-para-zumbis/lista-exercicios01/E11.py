'''
Exercício 11 - Python para Zumbis
-------------
Sabendo que str() converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
'''
print('QUANTOS DIGITOS EXISTEM EM 2^1.000.000')
print('=' * 30)
print()
num = 2**1000000
print(f'Dois elevado a um milhão => {len(str(num))} digitos. :D')
