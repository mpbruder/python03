num = int(input('Digite um numero inteiro: '))
print('\n{:=^23}'.format(' TABUADA DO {} '.format(num)), end='\n')
for c in range(1, 11):
    print('      {} x {:2} = {:2}'.format(num, c, (num * c)))
    c += 1
print('{:=^23}'.format('='))
