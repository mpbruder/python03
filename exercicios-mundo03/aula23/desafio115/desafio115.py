from time import sleep
from utilidades.cor import cores
from utilidades.strings import titulo
from utilidades.dado import opcao
from utilidades.cadastro import mostrarCadastros, cadastrarPessoa

tamanho = 40
dados = []

while True:
    titulo('MENU PRINCIPAL', tamanho)
    print(f'{cores["amarelo"]}1 - {cores["ciano"]}Ver pessoas cadastradas')
    print(f'{cores["amarelo"]}2 - {cores["ciano"]}Cadastrar nova pessoa')
    print(f'{cores["amarelo"]}3 - {cores["ciano"]}Sair do sistema{cores["limpa"]}')
    print('-' * tamanho)
    op = opcao(3)
    if op == 1:
        titulo('PESSOAS CADASTRADAS')
        mostrarCadastros('backupDado.txt')
        sleep(2)
    elif op == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        dados.append(nome)
        while True:
            idade = str(input('Idade: ')).strip()
            if idade.isnumeric():
                break
            else:
                print(f'{cores["vermelho"]}ERRO: Digite um número inteiro válido.{cores["limpa"]}')
        dados.append(idade)
        cadastrarPessoa(dados, 'backupDado.txt')
        dados.clear()
        sleep(2)
    elif op == 3:
        titulo('Saindo do sistema... Até logo!')
        sleep(1)
        break
