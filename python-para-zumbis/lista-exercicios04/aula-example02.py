data = str(input('Data (dd/mm/aaaa): ')).strip()
d, m, a = data.split('/')
meses = ['janeiro', 'fevereiro', 'março',
         'abril', 'maio', 'junho', 'julho', 'agosto',
         'setembro', 'outubro', 'novembro', 'dezembro']
print(f'{d} de {meses[int(m) - 1]} de {a}')
