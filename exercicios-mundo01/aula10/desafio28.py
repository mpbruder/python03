from random import randint
from time import sleep
print('-=-' * 14)
print('Pensei em um número. Consegue adivinhar?!')
print('-=-' * 14)
num = randint(0, 5)
var = int(input('Palpite: '))

print('PROCESSANDO...')
sleep(2)

if num != var:
    print('TENTE NOVAMENTE!')
else:
    print('PARABÉNS!')
print('Seu palpite foi {} e o número pensado pelo computador foi {}.'.format(var, num))
