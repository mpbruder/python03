somaPar = soma3C = maior2L = cont = 0
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
print('-=' * 30)

for lin in range(0, 3):
    for col in range(0, 3):
        # a) Somar pares
        if matriz[lin][col] % 2 == 0:
            somaPar += matriz[lin][col]

        # b) Somar terceira coluna
        if col == 2:
            soma3C += matriz[lin][col]

        # c) Maior elemento da segunda linha
        if lin == 1:
            if cont == 0:
                maior2L = matriz[lin][col]
                cont += 1
            else:
                if maior2L < matriz[lin][col]:
                    maior2L = matriz[lin][col]

print(f'A soma dos valores pares é {somaPar}.')
print(f'A soma dos valores da terceira coluna é {soma3C}.')
print(f'O maior elemento da segunda linha é {maior2L}.')
