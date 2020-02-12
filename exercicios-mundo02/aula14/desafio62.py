titulo = ' PROGRESSÃO ARITMÉTICA v3 '
print('\n{:=^35}'.format(titulo), end='\n')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

while razao == 0:
    razao = int(input('Dados inválidos. Insira outra razão para PA: '))

c = 1
totalTermos = 0
mais = 10
while mais != 0:
    totalTermos += mais
    while c < totalTermos:
        print('{} → '.format(termo), end='')
        termo += razao
        c += 1
    print('PAUSA\n', end='')
    mais = int(input(('Deseja ver mais quantos termos dessa PA? ')))
print('\nProgressão Aritmética finalizada com {} termos.'.format(totalTermos))
