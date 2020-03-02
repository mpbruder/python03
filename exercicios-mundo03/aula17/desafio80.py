numeros = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Valor adiconado ao final da numeros...')
    else:
        pos = 0
        while pos < len(numeros):  # Percorrer toda a numeros
            if num <= numeros[pos]:  # Inserir somente quando achar um maior
                numeros.insert(pos, num)
                print(f'Valos adicionado na posição {pos} da numeros...')
                break
            pos += 1

print('-=' * 40)
print(f'Os valores digitados em ordem foram: {numeros}')
