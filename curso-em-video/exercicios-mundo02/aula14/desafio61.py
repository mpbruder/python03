titulo = ' PROGRESSÃO ARITMÉTICA v2 '
print('\n{:=^35}'.format(titulo), end='\n')

c = 1
termo = int(input('Primeiro termo: '))
q = int(input('Razão: '))

while c < 11:
    print('{:2}º Termo: {:2}'.format(c, termo))
    c += 1
    termo += q

print('\tFIM')
