num = int(input('Digite um número: '))
opcao = int(input('Escolha base para transformação\n'
                  '\t[ 1 ] Binário\n'
                  '\t[ 2 ] Octal\n'
                  '\t[ 3 ] Hexadecimal\n'
                  ': '))
if opcao == 1:
    base = str('Binária').upper()
    convertido = bin(num)
elif opcao == 2:
    base = str('Octal').upper()
    convertido = oct(num)
elif opcao == 3:
    base = str('Hexadecimal').upper()
    convertido = hex(num)
else:
    print('Opção Inválida!')
    exit()  # Encerrar programa.
print('A conversão do número {} para base {} é {}.'.format(num, base, convertido[2:]))
