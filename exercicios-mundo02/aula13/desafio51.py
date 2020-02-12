titulo = ' PROGRESSÃO ARITMÉTICA '
print('\n{:=^35}'.format(titulo), end='\n')

i = int(input('Primeiro termo: '))
p = int(input('Razão: '))
ult = i + (10 * p)  # Formula para descobrir ultimo termo da PA!

for c in range(i, ult, p):
    print('{:2}º Termo: {:2}'.format(i + 1, c))
    i += 1
print('\tFIM')
