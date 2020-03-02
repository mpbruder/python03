from cor import estilos, cores

atleta = dict()
partidas = list()
jogadores = list()

quant = nGols = 0
while True:
    atleta.clear()
    partidas.clear()

    # Entrada de dados de cada atleta (dict())
    print(f'{estilos["negrito"]}{" DADOS JOGADOR ":=^50}{cores["limpa"]}')
    atleta['nome'] = str(input('Nome: ')).strip().capitalize()
    quant = int(input(f'Quantas partidas {atleta["nome"]} jogou? '))
    for c in range(0, quant):
        nGols = int(input(f'\t→ Quantos gols na partida {c + 1}? '))
        partidas.append(nGols)

    atleta['gols'] = partidas[:]
    atleta['total'] = sum(partidas)

    jogadores.append(atleta.copy())

    # Controle de encerramento
    while True:
        r = str(input(f'{estilos["negrito"]}Deseja continuar? [S/N]{cores["limpa"]} ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
print('\n')
print('*' * 50)
print(f'{" ESTATÍSTICA DOS JOGADORES ":^50}')
print('*' * 50)
print('Cód.  Nome\t\t\tTotal\t\tGols')
print('.' * 50)
for ixd, j in enumerate(jogadores):
    print(f'{ixd:<6}{j["nome"]:<16}{j["total"]:<10}{j["gols"]}')

while True:
    print('_' * 50)
    opc = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    if opc == 999:
        print('\tFINALIZANDO...')
        break
    elif opc not in range(0, len(jogadores)):
        print(f'Opção Inválida... Não há jogador com código {opc}. Tente novamente!')
        continue
    else:
        print(f'\t- LEVANTAMENTO JOGADOR {jogadores[opc]["nome"].upper()}:')
        if len(jogadores[opc]['gols']) == 0:
            print(f'\t\t→ {jogadores[opc]["nome"]} não jogou nenhuma partida.')
        for ixd, v in enumerate(jogadores[opc]["gols"]):
            print(f'\t\t→ No jogo {ixd + 1}, fez {v} gols.')
        print(f'\t+ Totalizando: {jogadores[opc]["total"]} gols.')

print('<<< VOLTE SEMPRE! >>>')
