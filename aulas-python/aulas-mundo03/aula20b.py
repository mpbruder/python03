def soma(a, b):
    s = a + b
    print(f'a = {a}; b = {b} → soma = {s}')


def somar(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando {valores} → soma = {s}')


# Programa principal
soma(1, 2)
soma(5, 3)
soma(b=7, a=2)
soma(a=4, b=6)
soma(5, 7)

somar(1, 3, 6)
somar(1, 5, 0, 6, 2)
somar(0)
