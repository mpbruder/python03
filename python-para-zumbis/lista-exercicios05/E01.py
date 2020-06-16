'''
Exercício 01 - Python para Zumbis
-------------
O que o seguinte programa (dado na forma de pseucódigo) imprime?

x = 2
y = 5
se y > 8 então
	y = y * 2
caso contrário,
	x = x * 2
imprime (x + y)
'''

x = 2
y = 5
if y > 8:
    y *= 2
else:
    x *= 2
print(f'Resposta: {x + y}')
