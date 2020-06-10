'''
Exercício 10 - Python para Zumbis
-------------
Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias. 
'''
print('TEMPO DE VIDA DE FUMANTE')
print()
cigarros_dia = int(input('Cigarros fumados por dia: '))
tot_anos = float(input('Total anos fumando: '))
# minutos perdidos em anos fumando
min_perdido = (cigarros_dia * 10) * (356 * tot_anos)
# Minutos por minutos em hora e hora em um dia
dias_perd = min_perdido // (60 * 24)
horas_perd = (min_perdido / (60 * 24) - dias_perd) * 24
# print(dias_perd)
# print(horas_perd)
print(f'Você perdeu ao todo {int(dias_perd)} dias e {int(horas_perd)} hora(s) de vida! :(')
