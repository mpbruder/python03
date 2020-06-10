from random import randint
from time import sleep
import emoji

itens = (emoji.emojize(':facepunch:', use_aliases=True),
         emoji.emojize(':raised_hand:', use_aliases=True),
         emoji.emojize(':v:', use_aliases=True))

print('Suas opções:\n'
      '[ 1 ] PEDRA\n'
      '[ 2 ] PAPEL\n'
      '[ 3 ] TESOURA\n')

jogador = int(input('Escolha sua jogada: '))
computador = randint(1, 3)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO\n\n')
sleep(0.5)

print('_' * 50)
print('\t\t\tJogador    VS    Computador\n'
      '\t\t\t  {}\t\t\t\t {}'.format(itens[jogador - 1], itens[computador - 1]))
print('_' * 50)

if computador == 1:
    if jogador == 1:
        print('\t*************** EMPATE! ***************')
    elif jogador == 2:
        print('\t**** PARABÉNS, VENCEU o computador ****')
    elif jogador == 3:
        print('\t********** Computador VENCEU *********')
    else:
        print('JOGADA INVÁLIDA!')
        exit()
elif computador == 2:
    if jogador == 1:
        print('\t********** Computador VENCEU *********')
    elif jogador == 2:
        print('\t*************** EMPATE! ***************')
    elif jogador == 3:
        print('\t**** PARABÉNS, VENCEU o computador ****')
    else:
        print('JOGADA INVÁLIDA!')
        exit()
else:
    if jogador == 1:
        print('\t**** PARABÉNS, VENCEU o computador ****')
    elif jogador == 2:
        print('\t********** Computador VENCEU *********')
    elif jogador == 3:
        print('\t*************** EMPATE! ***************')
    else:
        print('JOGADA INVÁLIDA!')
        exit()
