from cor import cores, estilos
from random import randint
from time import sleep
titulo = ' JOGO - Par ou Ímpar '
cont = 0

print('=' * 65)
print(f'{titulo:^65}')
print('=' * 65, end='\n')

while True:
    opcaoJogador = ' '
    while opcaoJogador not in 'PI':
        opcaoJogador = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))

    soma = computador + jogador

    print(f'{cores["azul"]}PROCESSANDO...\n\n')
    sleep(1)

    # Descobrir se é um número par ou ímpar
    if soma % 2 == 0:
        vencedor = 'P'
        aux = 'PAR!'
    else:
        vencedor = 'I'
        aux = 'ÍMPAR!'

    print(f'{cores["verde"]}{"-" * 65}{cores["limpa"]}')

    print(f'{cores["limpa"]}Você jogou {jogador} e o computador jogou {computador}, '
          f'{estilos["negrito"]}totalizando {soma} que é {aux}{cores["limpa"]}')

    print(f'{cores["verde"]}{"-" * 65}{cores["limpa"]}')

    if opcaoJogador == vencedor:
        print(f'{"VOCÊ VENCEU! Vamos jogar novamente...":^65}')
        print('\n')
        cont += 1
    else:
        print(f'{"VOCÊ PERDEU!":^65}')
        print('\n')
        break


print('=' * 65)
print(f'{cores["vermelho"]}', end='')
print(f'{"GAME OVER!":^65}')
print(f'{"Você venceu {} vezes...":^65}'.format(cont))
print(f'{cores["limpa"]}', end='')
print('=' * 65)
