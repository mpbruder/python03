galera = list()
dados = list()

for p in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])  # IMPEDE a 'ligação' entre listas, cria APENAS uma cópia.
    dados.clear()  # Limpar a lista temporaria 'dados'
for p in galera:
    if p[1] > 18:
        print(f'\n{p[0]} tem {p[1]}, portanto, é maior de idade.')
    else:
        print(f'\n{p[0]} tem {p[1]}, portanto, é menor de idade.')
print()
print(f'A lista \'galera\': {galera}')
