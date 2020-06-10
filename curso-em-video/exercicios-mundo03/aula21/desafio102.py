from time import sleep


def fatorial(n, show=False):
    """
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar a conta ou não.
    :return: O valor do fatorial de um número.
    Função criada por Matheus Bruder.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c != 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


# Programa Principal
print('-' * 30)
num = int(input('Calcular fatorial: '))
opc = ' '
while opc not in 'SN':
    opc = str(input('Deseja ver o cálculo? [S/N] ')).strip().upper()[0]
if opc == 'N':
    status = False
else:
    status = True
print('-' * 30)
print('PROCESSANDO...')
sleep(1)
print(fatorial(num, show=status))

# help(fatorial)
