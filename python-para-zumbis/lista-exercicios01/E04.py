'''
Exercício 04 - Python para Zumbis
-------------
Faça um programa que calcule o aumento de um salário. 
Ele deve solicitar o valor do salário e a porcentagem do aumento. 
Exiba o valor do aumento e do novo salário. 
'''
print('NOVO SALÁRIO')
print()
salario = float(input('Salário (R$): '))
aumento = float(input('Aumento (%): '))
if aumento <= 0:
    print('Insira uma porcentagem positiva')
    exit()
novo_sal = salario + (salario * (aumento / 100))
print(f'Salário antigo: R${salario:.2f}\nSalário atual: R${novo_sal:.2f}')
