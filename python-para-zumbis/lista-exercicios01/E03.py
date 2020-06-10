'''
Exercício 03 - Python para Zumbis
-------------
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
Calcule o total em segundos. 
'''
print('CÁLCULO EM SEGUNDOS')
print()
d = int(input('Dias: '))
h = int(input('Horas: '))
m = int(input('Minutos: '))
s = int(input('Segundos: '))

total = s + m * 60 + h * (60**2) + d * 24 * (60**2)

print(f'{d} dias; {h} horas; {m} minutos; {s} segundos => {total} segundos')
