t = float(input('Tempo (min): '))
if t < 200:
    preço = 0.2
else:
    if 200 <= t <= 400:
        preço = 0.18
    else:
        preço = 0.15
print(f'Total R${preço * t:.2f}')
