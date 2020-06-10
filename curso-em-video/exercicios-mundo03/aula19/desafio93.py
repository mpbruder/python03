jogador = dict()
partidas = list()

# Ler nome do jogador
jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()

# Criar laço para salvar os gols de cada jogo em uma lista
numPartida = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, numPartida):
    n = int(input(f'\t→ Quantos gols na partida {c + 1}? '))
    partidas.append(n)

# Copiar lista para o dicionario
jogador['gols'] = partidas[:]

# Salvar numero total de gols no dicionario
jogador['total'] = sum(partidas)

print('-=' * 40)
print(f'Dicionário: {jogador}')
print('-=' * 40)

# Mostrar as chaves e valores do dicionario
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 40)

# Mostrar o indice e os valores da lista qu esta no dicionario
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for ixd, c in enumerate(jogador['gols']):
    print(f'\t→ Na partida {ixd + 1}, fez {c} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
