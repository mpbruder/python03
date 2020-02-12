soma = quant = media = 0
resp = 'S'

while resp == 'S':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma / quant
print('Você digitou {} números e a média foi {:.2f}'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
