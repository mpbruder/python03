# Nova formatação do print - 'FSTRING'

nome = 'Matheus'
salario = 9954.4
idade = 20
print(f'O {nome:-^20} tem {idade} anos e recebe um salário de R${salario:.2f}!')              # PYTHON 3.6+

print('O {} tem {} anos e recebe um salário de R${:.2f}!'.format(nome, idade, salario))  # PYTHON 3+
print('O %s tem %d anos e recebe um salário de R$%.2f!' % (nome, idade, salario))        # PYTHON 2

