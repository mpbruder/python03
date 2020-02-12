print('{:=^60}'.format(' PRIMEIRO PROGRAMA COM MENU '))
opcao = 0

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

while opcao != 5:
    opcao = int(input(('\t[ 1 ] Somar\n\t[ 2 ] Multiplicar\n\t[ 3 ] Maior\n\t[ 4 ] Novos números\n\t[ 5 ] Exit\n\t> Opção: ')))
    # somar
    if opcao == 1:
        print('\tSOMA -> {} + {} = {}'.format(n1, n2, n1 + n2))
        print('-' * 30)

    # multiplicar
    elif opcao == 2:
        print('MULTIPLICAÇÃO -> {} x {} = {}'.format(n1, n2, n1 * n2))
        print('-' * 30)

    # maior
    elif opcao == 3:
        if n1 > n2:
            print('{} é MAIOR que {}.'.format(n1, n2))
            print('-' * 30)
        elif n2 > n1:
            print('{} é MAIOR que {}.'.format(n2, n1))
            print('-' * 30)
        else:
            print('{} é igual a {}, não há maior.'.format(n1, n2))
            print('-' * 30)

    # novos números
    elif opcao == 4:
        n1 = int(input('\n\nDigite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))

    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente!')
        print('-' * 30)

print('{:=^60}'.format(' Espero que tenha gostado! Até breve ...'))