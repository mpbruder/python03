print('=' * 30)
print('\t\tLOJAS MATNIC')
print('=' * 30)

preco = int(input('Preço das compras: R$ '))

pgmt = int(input('Escolha condição de pagamento\n'
                 '\t1 - Dinheiro ou Cheque\n'
                 '\t2 - Cartão\n'
                 ': '))
if pgmt == 1:
    desconto = preco * 0.9
    print('*' * 30)
    print('À VISTA - Dinheiro ou Cheque')
    print('*' * 30)
    print('DESCONTO: 10%\n'
          'TOTAL À PAGAR: {:.2f}'.format(desconto))
    print('-' * 30)
else:
    num_parc = int(input('\n\nEscolha o número de parcelas\n'
                         '\t1 - À Vista\n'
                         '\t2 - 2x\n'
                         '\t3 - 3x\n'
                         '\t...\n'
                         '\t12 - 12x\n'
                         ': '))
    if num_parc == 1:
        desconto = preco * 0.95
        print('*' * 30)
        print('Cartão - À VISTA')
        print('*' * 30)
        print('DESCONTO: 5%\n'
              'TOTAL À PAGAR: {:.2f}'.format(desconto))
        print('-' * 30)
    elif num_parc == 2:
        print('*' * 30)
        print('Cartão - 2x')
        print('*' * 30)
        print('VALOR PARCELA: R${:.2f}'.format(preco / num_parc))
        print('PARCELAS: 2x')
        print('TOTAL À PAGAR: {:.2f}'.format(preco))
        print('-' * 30)
    else:
        juros = preco * 1.2
        print('*' * 30)
        print('Cartão - 3x ou mais...')
        print('*' * 30)
        print('VALOR PARCELA: R${:.2f}'.format(juros / num_parc))
        print('PARCELAS: {}x'.format(num_parc))
        print('JUROS: 20%\n'
              'TOTAL À PAGAR: {:.2f}'.format(juros))
        print('-' * 30)
