# Docstrings
def contador(i, f, p):
    """
    É uma função responsável por realizar uma contagem,
    possui como parametros o inicio, fim e passo.
    :param i: Início da contagem
    :param f: Final da contagem
    :param p: Passo ou intervalo da contagem
    :return: Não há retorno
    Função criada por Matheus Bruder
    """
    for c in range(i, f + 1, p):
        print(f'{c}', end='..')
    print('FIM')


# Parametros Opcionais
def somar(a=0, b=0, c=0):
    """
    Função que soma até três valores
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    :return: Não há retorno
    Função criada por Matheus Bruder
    """
    s = a + b + c
    print(f'Soma vale {s}')

# Interactive Help - Usa docstrings!
help(print)
print('Olá, Mundo!')

# Usando docstings
contador(0, 100, 10)
help(contador)

# Usando parametros opcinais
somar(1, 0, 3)
somar(c=2, a=3)
somar(1, 5)
somar(0)
somar()
help(somar)

