'''
Exercício 05 - Python para Zumbis
-------------
Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar. 
'''
print('DESCONTO PRODUTO')
print()
prod = float(input('Valor produto (R$): '))
desc = float(input('Desconto (R$): '))
total = prod - (prod * (desc / 100))
print('=' * 30)
print(f'Total a pagar => R${total:.2f}')
