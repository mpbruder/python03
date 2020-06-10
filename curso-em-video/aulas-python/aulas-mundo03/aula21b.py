def teste():
    n1 = 9  # Escopo local
    print(f'N1 dentro (local) vale {n1}')


def teste2():
    global n1  # Impede a criação de outra variável "sombra"
    n1 = 10
    print(f'N1 dentro (global e local) vale {n1}')


# Programa Principal
n1 = 5  # Escopo global
teste()
print(f'N1 fora (global) vale {n1}')
teste2()
print(f'N1 fora (global) vale {n1}')
