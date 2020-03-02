a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))

numeros = (a, b, c, d)

print('- ' * 25)
print(f'Você digitou os valores: {numeros}')
print(f'O valor \'9\' apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor \'3\' apareceu na {numeros.index(3) + 1}º posição.')
else:
    print('O valor \'3\' não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')

pares = 0
for num in numeros:
    if num % 2 == 0 and num != 0:
        print(num, end=' ')
print('', end='\n')
