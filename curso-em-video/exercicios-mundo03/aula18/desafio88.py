from time import sleep
from random import randint

titulo = ' MEGA SENA '
lista = list()
jogo = list()

print('-' * 50)
print(f'{titulo:^50}')
print('-' * 50)

quant = int(input('Quantos quant deseja sortear? '))
print(f'=============== SORTEANDO {quant} JOGOS ===============')

# Gerar N jogos
for j in range(0, quant):
    # Gerar seis numeros aleatorios
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
        if len(jogo) == 6:
            break

    jogo.sort()
    lista.append(jogo[:])  # Copior a numeros 'jogo' para a numeros 'numeros'
    jogo.clear()  # Limpar numeros 'jogo'

# Mostrar na tela cada um dos elementos da 'numeros' (os quant)
for indx, jg in enumerate(lista):
    print(f'Jogo {indx + 1:2}: {lista[indx]}')
    sleep(0.8)
print(f'=================== BOA SORTE ===================')
