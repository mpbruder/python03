galera = list()
pessoa = dict()
sIdade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['sexo'] = s
    pessoa['idade'] = int(input('Idade: '))

    galera.append(pessoa.copy())

    # Controle encerramento
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break

print('-=' * 30)

# a) Quantidade de pessoas
print(f'\t→ O grupo tem {len(galera)} pessoas')

# b) Média de idade do grupo
for k, v in enumerate(galera):
    sIdade += v["idade"]
mIdade = sIdade / len(galera)
print(f'\t→ A média de idade é {mIdade:.2f}')

# c) Mulheres cadastradas
print(f'\t→ As mulheres cadastradas foram: ', end='')
for k, v in enumerate(galera):
    if v["sexo"] == 'F':
        print(f'[{v["nome"]}]', end=' ')
print()

# d) Lista pessoas acima da media de idade
print(f'\t→ Pessoas que estão acima da média [{mIdade:.2f}]:')
for individuo in galera:
    if individuo["idade"] > mIdade:
        for k, v in individuo.items():
            print(f'\t\t{k} = {v}', end='; ')
        print()

print('-=' * 30)
print('<< ENCERRADO >>')
