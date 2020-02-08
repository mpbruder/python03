numero = int(input('Digite um numero inteiro: '))
print('\n{:=^30}'.format(' TABUADA DO {} '.format(numero)), end='\n')
i = int(0)
while i < 11:
    print('{} x {:2} = {}'.format(numero, i, (numero * i)))
    i = i + 1
print('{:=^30}'.format('='))

