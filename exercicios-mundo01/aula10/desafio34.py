s = float(input('Qual salário o funcionário? '))
if s > 1250:
    print('\n#### Aumento de 10% ####')
    print('Salário: {:.2f}\nAumento: {:.2f}\nTotal: {:.2f}'.format(s, s * 0.10, s*1.10))
else:
    print('\n#### Aumento de 15% ####')
    print('Salário: {:.2f}\nAumento: {:.2f}\nTotal: {:.2f}\n'.format(s, s * 0.15, s * 1.15))
print('Bom trabalho!')
