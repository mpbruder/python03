# comando usando WHILE
resp = 's'
par = impar = 0

while resp != 'n':
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    resp = str(input(('Deseja continuar? [S/N]: '))).lower()
print('\nTOTAL PARES: {}\nTOTAL ÍMPARES: {}'.format(par, impar))

# comando usando FOR

# IMPOSSÍVEL USAR FOR!!!
