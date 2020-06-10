from cor import cores
stringMinuscula = str(input('Digite uma frase: ').strip().lower())

# Remover os espaços entre palavras
vetorPalavras = stringMinuscula.split()
stringSemEspaco = ''.join(vetorPalavras)

# Inverter a string
stringInvertida = stringSemEspaco[::-1]

# Verificar se é palíndromo
if stringSemEspaco == stringInvertida:
    print('{}'.format(cores['verde']))
    print(stringSemEspaco)
    print(stringInvertida)
    print('{}'.format(cores['limpa']))
    print('É um palíndromo.')
else:
    print('{}'.format(cores['vermelho']))
    print(stringSemEspaco)
    print(stringInvertida)
    print('{}'.format(cores['limpa']))
    print('NÃO é um palíndromo.')