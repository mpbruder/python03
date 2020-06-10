'''
Exercício 02 - Python para Zumbis
-------------
Determine se um ano é bissexto. Verifique no Google como fazer isso... 
'''
import calendar
a = int(input('Ano: '))
if calendar.isleap(a) == True:
    print(f'{a} É BISSEXTO!')
else:
    print(f'{a} NÃO É BISSEXTO!')
