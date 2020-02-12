n1 = float(input('Nota P1: '))
n2 = float(input('Nota P2: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('REPROVADO - Média foi {:.2f}'.format(m))
elif m >= 5.0 and m < 7.0:
    print('EXAME - Média foi {:.2f}'.format(m))
else:
    print('APROVADO - Média foi {:.2f}'.format(m))