print('{:=^50}'.format(' FATORIAL FOR '))
num = int(input('Calcular o fatorial: '))
c = num
f = 1
print('{}! = '.format(num), end='')
for c in range(num, 0, -1):
    if c != 1:
        print('{} x '.format(c), end='')
    else:
        print('{} = '.format(c), end='')
    f *= c
    c -= 1
print(f)