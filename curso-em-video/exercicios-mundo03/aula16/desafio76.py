listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.3, 'Livros', 34.9)

print('-' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-' * 50)

lim = int(len(listagem))
for i in range(0, lim, 2):
    # '.<40' - significa que é para alinhar 40 caracteres à esquerda
    print(f'{listagem[i]:.<40}', end='')
    # '>8.2f' - significa que é para alinhar 8 caracteres à direita E mostrar o número com 2 casas decimais
    print(f'R${listagem[i + 1]:>8.2f}')

print('_' * 50)
