s = 0
b = 0

for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        print(c)
        s += c
        b += 1

print('Somatório dos {} valores é igual a {}.'.format(b, s))
