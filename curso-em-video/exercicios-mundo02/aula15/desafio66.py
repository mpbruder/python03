from cor import cores
quant = sum = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    sum += num
    quant += 1
print(f'A soma dos {cores["amarelo"]}{quant} valores{cores["limpa"]} foi {cores["azul3"]}{sum}{cores["limpa"]}!')
