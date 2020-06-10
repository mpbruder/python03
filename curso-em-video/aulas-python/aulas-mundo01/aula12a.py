# 'elif' indica que há mais de uma possibilidade... Imagine 3 caminhos distintos!
nome = str(input('Qual é seu nome? ')).strip()
if nome == 'Matheus':
    print('Que belo nome!')
elif nome in 'Maria Paula Joana Joaquina Jade Bernadete Neusa Claudia':
    print('Seu nome é feminino!')
elif nome in 'Marcos Marcelo Pedro Lucas Tadeu João Gabriel':
    print('Seu nome é masculino!')
else:
    print('Tenha um bom dia, {}!'.format(nome))
