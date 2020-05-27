def titulo(msg, cor='\033[m'):
    tam = len(msg) + 4
    print(f'{cor}~' * tam)
    print(f'  {msg}')
    print(f'~' * tam)
    print('\033[m', end='')


def ajuda(cmd):
    from time import sleep
    titulo(f'Acessando o manual do comando \'{cmd}\'', '\033[0;30;45m')
    sleep(1)
    print('\033[7;30m', end='')
    help(cmd)
    print('\033[m', end='')
    sleep(1)


# Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', '\033[1;30;43m')
    comando = str(input('Função ou Biclioteca >> ')).strip().lower()
    if comando == 'fim':
        titulo(f'ATÉ LOGO!', '\033[1;30;41m')
        break
    else:
        ajuda(comando)
