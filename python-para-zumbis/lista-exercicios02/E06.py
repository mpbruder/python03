'''
Exercício 06 - Python para Zumbis
-------------
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, 
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. 
Calcule os descontos e o salário líquido, conforme a tabela abaixo: 
	a. + Salário Bruto : R$ 
	b. - IR (11%) : R$ 
	c. - INSS (8%) : R$ 
	d. - Sindicato ( 5%) : R$ 
	e. = Salário Liquido : R$ 
'''
h = int(input('Ganho por hora (R$): '))
nh = int(input('Horas trabalhadas no mês: '))
s_bruto = h * nh
IR = s_bruto * 0.11
INSS = s_bruto * 0.08
SIND = s_bruto * 0.05
print(f'+ SALÁRIO BRUTO: R${s_bruto:.2f}')
print(f'- IR (11%): R${IR:.2f}')
print(f'- INSS (8%): R${INSS:.2f}')
print(f'- SINDICATO (5%): R${SIND:.2f}')
print(f'= SALÁRIO LÍQUIDO: R${s_bruto - IR - INSS - SIND:.2f}')
