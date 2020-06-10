from utilidades import moeda

v = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(v)} é {moeda.metade_formatacao(v, True)}')
print(f'O dobro de {moeda.moeda(v)} é {moeda.dobro_formatacao(v, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar_formatacao(v, 10, False)}')
print(f'Reduzindo 13%, temos {moeda.diminuir_formatacao(v, 13)}')
