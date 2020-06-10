n = 0
soma = 0
while True:
    x = int(input('n (zero sai): '))
    if x == 0:
        break
    else:
        n += 1
        soma += x
print(f'Soma: {soma}')
print(f'Média: {soma / n:.1f}')
