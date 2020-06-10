print('-' * 26)
print('CALCULADORA DE EMPRÉSTIMO')
print('-' * 26 + '\n')

valor = float(input('Valor da casa: '))
salario = float(input('Salário atual: '))
anos = int(input('Número de anos para pagar: '))

num_parcelas = int(anos * 12)
valor_parcela = valor / num_parcelas
porcentagem = float(salario * 0.3)

if valor_parcela > porcentagem:
    print('\nEmpréstimo negado... Dívida mensal maior que 30% do salário!')
    print('NUMERO PARCELAS: {}x'.format(num_parcelas))
    print('VALOR PARCELA: R${:.2f}'.format(valor_parcela))
elif valor_parcela == porcentagem:
    print('\nEmpréstimo concedido, mas tome cuidado, parcelas caras...')
    print('NUMERO PARCELAS: {}x'.format(num_parcelas))
    print('VALOR PARCELA: R${:.2f}'.format(valor_parcela))
else:
    print('\nEmpréstimo concedido, parabéns!')
    print('NUMERO PARCELAS: {}x'.format(num_parcelas))
    print('VALOR PARCELA: R${:.2f}'.format(valor_parcela))
