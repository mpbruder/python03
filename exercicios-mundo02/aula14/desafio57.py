import emoji
sexo = str(input('Qual seu sexo? [M/F]? ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Insira seu sexo novamente [M/F]: ')).strip().upper()[0]
if sexo == 'F':
    print(emoji.emojize('Sexo Feminino registrado. :woman:'))
else:
    print(emoji.emojize('Sexo masculino registrado. :man:'))
