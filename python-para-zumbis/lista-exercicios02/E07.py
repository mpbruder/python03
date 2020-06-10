'''
Exercício 07 - Python para Zumbis
-------------
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
Obs. : somente são vendidos um número inteiro de latas. 
'''
a = float(input('Área (m²): '))
a_lata = 18 * 3  # 54m²/lata
latas = int(a // a_lata)
resto = a % a_lata
if resto != 0:
    latas += 1
print(f'QTND LATAS: {latas}')
print(f'PREÇO: R$ {latas * 80:.2f}')
