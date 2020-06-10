# LIMITE CONHECIDO → FOR ou WHILE
cont = 1
while cont < 11:
    print(cont, end=' → ')
    cont += 1
print('Acabou')

# LIMITE DESCONHECIDO → WHILE
n = 0
while n != 999:
    n = int(input('Digite um número: '))
print('Acabou')

# LIMITE DESCONHECIDO COM BREAK → WHILE
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
