from utilidades import moeda

v = float(input('Digite o preço: '))
print(f'A metade de {v} é {moeda.metade(v)}')
print(f'O dobro de {v} é {moeda.dobro(v)}')
print(f'Aumentando 10%, temos {moeda.aumentar(v, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(v, 13)}')
