palavra = str(input('Palavra: ')).strip()  # retirar espaços
reverse = palavra[::-1]  # Inverter palavra
if palavra.lower() == reverse.lower():  # tornar minusculo
    print(f'{palavra} == {reverse}')
else:
    print(f'{palavra} != {reverse}')
