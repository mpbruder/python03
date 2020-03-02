# LIGAÇÃO ENTRE LISTAS
print('Listas com ligação')
a = [0, 1, 2, 3, 4]
b = a  # cria uma ligação entra as duas listas
b[0] = 99
print(f'Lista A: {a}')
print(f'Lista B: {b}\n\n')

# CÓPIA ENTRE LISTAS
print('Cópia entre listas')
a = [0, 1, 2, 3, 4]
b = a[:]  # apenas copia todos elementos
b[0] = 99
print(f'Lista A: {a}')
print(f'Lista B: {b}')
