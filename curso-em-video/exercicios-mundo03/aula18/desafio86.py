# Declaração da Matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Leitura dos valores
for lin in range(0, 3):
    for col in range(0, 3):
        valor = int(input(f'Digite um valor para [{lin}, {col}]: '))
        matriz[lin][col] = valor

print('-=' * 30)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[ {matriz[lin][col]:^4} ]', end='')
    print()
