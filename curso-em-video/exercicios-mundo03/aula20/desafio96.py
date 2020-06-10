def titulo():
    print('-' * 30)
    print(f'{"CONTROLE DE TERRENO":^30}')
    print('-' * 30)


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é {a:.2f}m²')


# Programa Principal
titulo()
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
