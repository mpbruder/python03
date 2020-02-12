soma = 0
count = 0
for c in range(0, 6):
    num = int(input('Digite {}º número inteiro: '.format(c + 1)))
    if num % 2 == 0:
        soma += num
        count += 1
print('\nSomatório dos {} números pares foi {}.'.format(count, soma))
