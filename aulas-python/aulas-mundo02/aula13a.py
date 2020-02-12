i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))  # Passo = '-1' contagem do final para o começo
for c in range(i, f, p):
    print(c)
