print('{:=^50}'.format(' FATORIAL WHILE'))
num = int(input('Calcular o fatorial: '))
c = num
f = 1
print('{}! = '.format(num), end='')
while c > 0:
    if c != 1:
        print('{} x '.format(c), end='')
    else:
        print('{} = '.format(c), end='')
    f *= c
    c -= 1
print('{}'.format(f))
