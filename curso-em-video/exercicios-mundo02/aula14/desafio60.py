from math import factorial
print('{:=^50}'.format(' FATORIAL '))
num = int(input('Calcular o fatorial: '))
fat = factorial(num)
print('{}! = {}'.format(num, fat), end='')


