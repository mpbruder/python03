def fatorial(n):
    """
    Calcular fatorial de um número.
    :param n: Número que deseja calcular fatorial.
    :return: Fatorial de 'n'.
    """
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n):
    """
    Calcula dobro de um número.
    :param n: Número que deseja calcular o dobro.
    :return: O dobro do número 'n'.
    """
    n *= 2
    return n


def triplo(n):
    """
    Calcula o triplo de um número.
    :param n: Número que deseja calcular o triplo.
    :return: O triplo do número 'n'.
    """
    n *= 3
    return n
