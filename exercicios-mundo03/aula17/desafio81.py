numeros = list()

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

# a) Quantos numeros foram adicionados
print(f'Você digitou {len(numeros)} elementos.')

# b) Ordenar de forma decrescente
numeros.sort(reverse=True)
print(f'Lista ordenada de forma decrescente: {numeros}')

# c) Valor 5 esta ou não na numeros
if 5 in numeros:
    print('O valor \'5\' está na numeros!')
else:
    print('O valor \'5\' NÃO ESTÁ na numeros!')
