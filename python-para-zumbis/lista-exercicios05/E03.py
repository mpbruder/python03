'''
Exercício 03 - Python para Zumbis
-------------
Entre 1067 e 3627 (inclusive), quantos números são pares e também divisíveis por 7? 
'''
s = 0
for i in range(1067, 3628):
    if (i % 2 == 0) and (i % 7 == 0):
        s += 1
        # print(f'{i}')
print(f'Resposta: {s}')
