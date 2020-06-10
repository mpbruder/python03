estado = dict()
brasil = list()
for c in range(0, 2):
    estado['nome'] = str(input('Estado: ')).strip().capitalize()
    estado['sigla'] = str(input('Sigla: ')).strip().upper()[0:2]
    brasil.append(estado.copy())

for est in brasil:
    for v in est.values():
        print(f'{v}', end=' ')
    print()

print(brasil)