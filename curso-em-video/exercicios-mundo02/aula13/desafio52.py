from cor import cores
num = int(input('Digite um número inteiro: '))
count = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(cores['amarelo'], end=' ')
        count += 1
    else:
        print(cores['vermelho'], end=' ')
    print(c, end=' ')

print('\n{}O número {} foi divisível {} vezes.'.format(cores['limpa'], num, count))
if count > 2:
    print('E por isso{} NÃO é primo.{}'.format(cores['vermelho'], cores['limpa']))
else:
    print('E por isso{} É PRIMO.{}'.format(cores['verde'], cores['limpa']))
