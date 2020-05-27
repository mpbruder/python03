def ficha(n='<desconhecido>', g=0):
    """
    Função que mostra ficha de um jogador de futebol.
    :param n: Nome do jogador.
    :param g: Quantidade de gols do jogador em sua carreira.
    :return:
    """
    print(f'O jogador {n} fez {g} gol(s) no campeonato')


# Programa principal
nome = str(input('Nome do jogador: ')).capitalize().strip()
nGols = str(input('Número de gols: '))

# Validações dos dados
if nGols.isnumeric():
    nGols = int(nGols)
else:
    nGols = 0
if nome.strip() == '':
    ficha(g=nGols)
else:
    ficha(n=nome, g=nGols)
