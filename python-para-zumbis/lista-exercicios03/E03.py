'''
Exercício 03 - Python para Zumbis
-------------
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e 
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale 
a população do país B, mantidas as taxas de crescimento
'''
import datetime
anos = 0
cresc_A, pop_A = 1.030, 80000
cresc_B, pop_B = 1.015, 200000
while pop_A <= pop_B:
    pop_A *= cresc_A
    pop_B *= cresc_B
    anos += 1
atual = datetime.datetime.now()
print(f'Em {atual.year + anos} após {anos} (contando de hoje) população de A será igual de B.')
