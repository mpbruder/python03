from random import randint
from time import sleep
from operator import itemgetter

dicio = dict()
ranking = dict()
numJogadores = 4

# Alimentando dicionario
for c in range(0, numJogadores):
    dicio[f'jogador{c + 1}'] = randint(1, 6)

# Printando valores dos dados de cada jogador
print(f'{" Valores Sorteados ":=^40}')
for k, v in dicio.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)

# Printando ranking dos jogadores de acordo com valor do dado
print(f'\n{" Ranking ":=^40}')
ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True)  # Ordenar dicionario
for ixd, v in enumerate(ranking):
    print(f'{ixd + 1}º lugar: {v[0]} com o número {v[1]}.')
    sleep(1)
