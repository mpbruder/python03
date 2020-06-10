pessoa = dict()

pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
pessoa['media'] = float(input(f'Média de {pessoa["nome"]}: '))
if pessoa['media'] >= 7:
    pessoa['situacao'] = 'Aprovado'
elif 5 <= pessoa['media'] < 7:
    pessoa['situacao'] = 'Recuperação'
else:
    pessoa['situacao'] = 'Reprovado'
print('-=' * 20)
for k, v in pessoa.items():
    print(f'\t- {k.capitalize()} é igual a {v}')
