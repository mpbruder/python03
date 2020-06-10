numeros = list()
for cont in range(0, 5):
    n = int(input(f'Digite um valor para a posição {cont}: '))
    numeros.append(n)
print('-=' * 40)
print(f'Você digitou os valores: {numeros}')

# Maior e menor valores com respectivas posições.
# Maior valor
print(f'O maior valor digitado foi {max(numeros)} nas posições ', end='')
for indx, num in enumerate(numeros):
    if num == max(numeros):
        print(f'{indx}...', end=' ')

# Menor valor
print(f'\nO menor valor digitado foi {min(numeros)} nas posições ', end='')
for indx, num in enumerate(numeros):
    if num == min(numeros):
        print(f'{indx}...', end=' ')
