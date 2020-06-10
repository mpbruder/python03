lista = list()
aluno = list()
notas = list()

# Looping para cadastro dos alunos e notas
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    aluno.append(nome)
    n1 = float(input('Nota 01: '))
    notas.append(n1)
    n2 = float(input('Nota 02: '))
    notas.append(n2)
    med = (n1 + n2) / 2
    notas.append(med)

    # Criar copia da numeros para um nivel superior
    aluno.append(notas[:])
    lista.append(aluno[:])

    # Limpar 'notas' e 'aluno'
    notas.clear()
    aluno.clear()

    # Controle de encerramento
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 30)

# Mostrar boletim com todos alunos e médias
print('-' * 42)
print('No.\t\t\t\tNome\t\t\t\tMÉDIA')
print('-' * 42)
for ixd, p in enumerate(lista):
    print(f'{ixd:<16}{p[0]:<20}{p[1][2]:>4.1f}')
print('_' * 42)

# Mostrar a nota de cada um dos alunos
while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    # Condicao de parada
    if opcao == 999:
        print('FINALIZANDO...')
        break
    # Condicao de amostragem
    if opcao in range(0, len(lista)):
        print(f'Notas de {lista[opcao][0]} são {lista[opcao][1][0]} e {lista[opcao][1][1]}')
        print('-' * 40)
    # Tratamento de erro
    else:
        print('Aluno não cadastrado... Tente novamente!')
        print('-' * 40)
print('<< VOLTE SEMPRE >>')
