'''
Exercício 02 - Python para Zumbis
-------------
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações. 
'''
nome = input('Nome: ').strip()
senha = input('Senha: ').strip()
while nome == senha:
    print(f'Dados inválidos, repita...')
    nome = input('Nome: ').strip()
    senha = input('Senha: ').strip()
