'''
Exercício 09 - Python para Zumbis
-------------
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado. 
'''
print('ALUGUEL CARRO')
print()
dist = float(input('Distância percorrida (km): '))
dias = 0
while dias < 1:  # nao posso alugar um carro somente por distancia
    dias = int(input('Tempo aluguel (dias): '))
preco = 60 * dias + 0.15 * dist
print('=' * 25)
print(f'Total a pagar: R${preco:.2f}')
