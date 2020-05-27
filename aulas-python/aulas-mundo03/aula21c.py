def fatorial(num=1):
    """
    Função que calcula o fatorial de um número
    :param num: Número que deseja obter o fatorial
    :return: O fatorial
    Função criada por Matheus Bruder
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


# Programa Principal
n = int(input('Digite um número: '))
print(f'Fatorial de {n} vale {fatorial(n)}')
