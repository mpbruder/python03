n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.2f}'.format(m))
if m < 2.5:
    print('REPROVADO!')
elif 2.5 <= m < 6:
    print('EXAME!')
else:
    print('APROVADO!')
