from datetime import date
trabalhador = dict()

nome = str(input('Nome: ')).strip().capitalize()
anoNasc = int(input('Ano de Nascimento: '))
anoAtual = date.today().year
carteira = int(input('Carteira de Trabalho (0 não tem): '))

trabalhador['nome'] = nome
trabalhador['idade'] = anoAtual - anoNasc
trabalhador['ctps'] = carteira
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] = (35 - (anoAtual - trabalhador['contratação'])) + trabalhador['idade']

print('-=' * 20)

# Mostrar todos os valores
for k, v in trabalhador.items():
    print(f'\t- {k.upper()} tem valor {v}')
print(trabalhador)
