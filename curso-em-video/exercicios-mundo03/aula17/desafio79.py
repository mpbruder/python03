numeros = list()
while True:
    num = int(input('Digite um valor: '))
    if num in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        numeros.append(num)

    # Controle encerramento do programa
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 40)
numeros.sort()
print(f'Você digitou os valores: {numeros}')
