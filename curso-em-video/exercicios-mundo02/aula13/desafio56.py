lim = 4
totAnos = 0
nomeVelho = '-------'
idadeVelho = 0
contador = 0

for c in range(0, lim):
    print('{:-^25}'.format(' {}ª PESSOA '.format(c + 1)))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    # Sumarizações e Cálculos
    # a) Média de idade
    totAnos += idade
    medAnos = totAnos / lim

    # b) Homem mais velho
    if c == 1 and sexo == 'M':
        nomeVelho = nome
        idadeVelho = idade
    if c != 1 and sexo == 'M':
        if idade > idadeVelho:
            idadeVelho = idade
            nomeVelho = nome

    # c) Quantas mulheres tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        contador += 1

print('\nA média de idade do grupo é de {} anos.'.format(medAnos))
print('O homem mais velho tem {} anos e se chama {}.'.format(idadeVelho, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(contador))
