n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('{} é maior\n{} é menor.'.format(n1, n2))
elif n2 > n1:
    print('{} é maior\n{} é menor.'.format(n2, n1))
else:
    print('Não existe valor maior, ambos são iguais!')
