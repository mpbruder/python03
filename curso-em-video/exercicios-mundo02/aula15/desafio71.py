from cor import cores, estilos

titulo = ' NUBANK '

print(f'{cores["roxo"]}{estilos["negrito"]}', end='')
print('=' * 40)
print(f'{titulo:^40}')
print('=' * 40, end='\n')
print(f'{cores["limpa"]}', end='\n')

valor = int(input('Qual valor deseja sacar? R$ '))
total = valor
cedAtual = 50
totalCedula = 0

while True:
    if total >= cedAtual:
        total -= cedAtual
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${cedAtual}')

        totalCedula = 0

        if cedAtual == 50:
            cedAtual = 20
        elif cedAtual == 20:
            cedAtual = 10
        elif cedAtual == 10:
            cedAtual = 1

        if total == 0:
            break

print(f'{cores["roxo"]}{estilos["negrito"]}', end='')
print('=' * 40)
print(f'{"Nubank Agradece!":^40}')
