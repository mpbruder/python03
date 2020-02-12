limite = 5
maior = 0
menor = 0

for c in range(0, limite):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c + 1)))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('Maior peso lido foi {}Kg.'.format(maior))
print('Menor peso lido foi {}Kg.'.format(menor))
