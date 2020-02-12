from cor import cores, estilos
from random import randint
from time import sleep

print('-=-' * 19)
print('Pensei em um número entre 0 e 10. Consegue adivinhar?!')
print('-=-' * 19)
computador = randint(0, 10)
jogador = 11
palpites = 1

while jogador != computador:
    jogador = int(input('Palpite: '))
    print('{}{}PROCESSANDO...{}'.format(cores['azul'], estilos['negrito'], cores['limpa']))
    sleep(1.5)
    if jogador != computador:
        if jogador > computador:
            print('Menos... Tente novamente!')
        else:
            print('Mais... Tente novamente!')
        palpites += 1
print('PARABÉNS!!! Você precisou de {}{} tentativas{} para acertar.'.format(cores['amarelo'], palpites, cores['limpa']))
