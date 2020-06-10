n = 1
soma = 0
while n <= 10	:
    x = int(input(f'{n} número: '))
    soma += x
    n += 1
print(f'Soma: {soma}')
print(f'Média: {soma / (n - 1):.1f}')
