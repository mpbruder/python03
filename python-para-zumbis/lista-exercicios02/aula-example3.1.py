t = float(input('Tempo (min): '))
if t < 200:
    preço = 0.2
elif t <= 400:
    preço = 0.18
elif t <= 800:
    preço = 0.15
else:
    preço = 0.08
print(f'Total R${preço * t:.2f}')
