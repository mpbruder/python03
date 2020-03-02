from random import randint
limite = 10
a = randint(0, limite)
b = randint(0, limite)
c = randint(0, limite)
d = randint(0, limite)
e = randint(0, limite)
numeros = (a, b, c, d, e)
# print(len(numeros))
# precisa-se iniciar as duas variaveis com um numero, melhor que seja o primeiro

# maior = menor = a
print('Os valores sorteados foram: ', end='')
for num in numeros:
    print(num, end=' ')

# Comparações para descobrir maior e menor
print(f'\nMaior valor sorteado foi {max(numeros)}')
print(f'Menor valor sorteado foi {min(numeros)}')

'''
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'\nMaior valor sorteado foi {maior}')
print(f'Menor valor sorteado foi {menor}')
'''

