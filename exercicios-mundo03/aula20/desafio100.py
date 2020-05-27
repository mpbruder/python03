from random import randint
from time import sleep


def sorteia():
    print('Sorteando os 5 valores da lista: ', end='')
    for c in range(0, 5):
        num = randint(1, 10)
        print(num, end=' ')
        sleep(0.5)
        lista.append(num)
    print()


def somaPar(lst):
    s = 0
    for num in lst:
        if num % 2 == 0:
            s += num
    print(f'O somaatório do pares da lista {lista} é {s}')


# Programa principal
lista = []
sorteia()
somaPar(lista)
