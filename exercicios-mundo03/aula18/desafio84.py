dados = list()
pessoas = list()
cont = gordo = magro = 0

while True:
    nome = str(input('Nome: ')).strip().capitalize()
    peso = float(input('Peso: '))

    if cont == 0:
        gordo = magro = peso
        cont += 1
    else:
        if peso >= gordo:
            gordo = peso
        if peso <= magro:
            magro = peso

    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()  # Limpar numeros 'dados'

    # Controle termino do programa
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break

print('-=' * 40)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'Maior peso foi {gordo:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == gordo:
        print(f'[{p[0]}]', end=' ')
print()
print(f'Menor peso foi {magro:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == magro:
        print(f'[{p[0]}]', end=' ')
print()
