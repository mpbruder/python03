'''
Exercício 03 - Python para Zumbis
-------------
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. 
Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. 
Caso contrário mostrar tais variáveis com o conteúdo ZERO. 
'''
p = float(input('Peso (Kg): '))
multa = 0.0
excesso = 0.0
if p > 50:
    excesso = p - 50
    multa = 4 * excesso
    print(f'MULTA R$ {multa:.2f}')
    print(f'EXCESSO {excesso:.2f} Kg')
else:
    print(f'MULTA R$ {multa:.2f}')
    print(f'EXCESSO {excesso:.2f} Kg')
