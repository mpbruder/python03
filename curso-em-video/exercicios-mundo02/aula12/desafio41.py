from datetime import date

nasc = int(input('Ano de nascimento do atleta: '))
ano = date.today().year
idade = ano - nasc
print(' ***************************** \n')
print('IDADE: {}'.format(idade))
if idade <= 9:
    print('CATEGORIA: Mirim')
    print('LIMITE: 9 anos')
elif idade <= 14:
    print('CATEGORIA: Infantil')
    print('LIMITE: 14 anos')
elif idade <= 19:
    print('CATEGORIA: Junior')
    print('LIMITE: 19 anos')
elif idade <= 20:
    print('CATEGORIA: Sênior')
    print('LIMITE: 20 anos')
else:
    print('CATEGORIA: Master')
    print('LIMITE: Última categoria')
