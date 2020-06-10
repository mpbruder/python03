times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro',
         'CSA', 'Chapecoense', 'Avaí')

print(f'TABELA DE TIMES DO BRASILEIRÃO 2019:\n{times}\n')
print(f'Primeiros 5 colocados:\n{times[0:5]}\n')
print(f'Últimos 4 colocados:\n{times[-4:]}\n')
print(f'Ordem alfabética:\n{sorted(times)}\n')
print(f'Time \'Chapecoense\' está na posição: {times.index("Chapecoense") + 1}º\n')  # '+1' por causa do 0...
