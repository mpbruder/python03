numeros = list()
pares = list()
impares = list()
while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)

    # Controle encerramento do programa
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 40)

# Tratamento e criação das listas par e impar
for i in numeros:
    if i == 0:
        continue
    elif i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

# Lista completa
print(f'A lista completa é {numeros}')

# Lista dos pares
pares.sort()
print(f'A lista dos pares é {pares}')

# Lista dos impares
impares.sort()
print(f'A lista dos ímpares é {impares}')
