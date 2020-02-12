titulo = ' Cadastro de Pessoas '
totM20 = totH = tot18 = 0

print(f'{titulo:=^40}')

while True:
    # Ler dados do usuário
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    # a) > 18 anos
    if idade > 18:
        tot18 += 1
    # b) Contar homens
    if sexo == 'M':
        totH += 1
    # c) Contar mulheres com < 20 anos
    if sexo == 'F' and idade < 20:
        totM20 += 1

    # Ponto de decisão de parada
    print('-' * 30)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('-' * 30)

    # STOP: Execução do Laço
    if opcao == 'N':
        break

print(f'{" Fim do Programa ":=^40}')

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {totH}')
print(f'Total de mulheres com menos de 20 anos: {totM20}')
