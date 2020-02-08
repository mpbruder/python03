from datetime import date
ano = int(input('Analise o ano. Para analisar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano Bissexto!'.format(ano))
else:
    print('{} NÃO é um ano Bissexto!'.format(ano))
